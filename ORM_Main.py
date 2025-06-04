import cv2
import numpy as np
import os
from pdf2image import convert_from_path
import json
import shutil
from datetime import datetime

# Diretórios fixos no disco
BASE_INPUT_DIR = r"C:\OMR\gabaritos\entrada"
BASE_OUTPUT_DIR = r"C:\OMR\gabaritos\saida"

# Cria diretórios se não existirem
os.makedirs(BASE_INPUT_DIR, exist_ok=True)
os.makedirs(BASE_OUTPUT_DIR, exist_ok=True)

def sanitize_filename(filename):
    # Remove ou substitui caracteres que podem causar problemas
    return "".join(c if c.isalnum() or c in [' ', '_', '-'] else "_" for c in filename)

def process_pdf(input_pdf_path, upload_id=1):  # parâmetro upload_id adicionado
    pdf_name_raw = os.path.splitext(os.path.basename(input_pdf_path))[0]
    pdf_name = sanitize_filename(pdf_name_raw)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    session_id = f"{pdf_name}_{timestamp}"

    base_dir = os.path.join(BASE_OUTPUT_DIR, session_id)
    jpeg_dir = os.path.join(base_dir, "jpeg")
    cutouts_dir = os.path.join(base_dir, "cutouts")
    json_dir = os.path.join(base_dir, "json")
    matricula_dir = os.path.join(base_dir, "matricula")

    for d in [jpeg_dir, cutouts_dir, json_dir, matricula_dir]:
        os.makedirs(d, exist_ok=True)

    print(f"Convertendo PDF em imagens: {input_pdf_path}")
    pages = convert_from_path(input_pdf_path, dpi=300)
    
    # Vamos montar um dicionário para agrupar resultados por página e coluna
    resultado = []
    
    for page_idx, page in enumerate(pages):
        jpeg_path = os.path.join(jpeg_dir, f"page_{page_idx + 1}.jpeg")
        page.save(jpeg_path, "JPEG")

        img = cv2.imread(jpeg_path)
        if img is None:
            print(f"Erro: Não foi possível ler a imagem salva em {jpeg_path}")
            continue

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 1)
        canny = cv2.Canny(blur, 10, 30)

        contours, _ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        rectangles = []
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 5000:
                peri = cv2.arcLength(cnt, True)
                approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
                if len(approx) == 4:
                    rectangles.append(approx)

        def ordenar_pontos(pontos):
            pontos = pontos.reshape(4, 2)
            soma = pontos.sum(axis=1)
            diff = np.diff(pontos, axis=1)
            ordenado = np.zeros((4, 2), dtype="float32")
            ordenado[0] = pontos[np.argmin(soma)]
            ordenado[2] = pontos[np.argmax(soma)]
            ordenado[1] = pontos[np.argmin(diff)]
            ordenado[3] = pontos[np.argmax(diff)]
            return ordenado

        recortes_info = []
        for rect in rectangles:
            x, y, w, h = cv2.boundingRect(rect)
            recortes_info.append({"x": x, "y": y, "w": w, "h": h, "rect": rect})

        recortes_info = sorted(recortes_info, key=lambda r: (r["y"], -r["w"]))
        if not recortes_info:
            #print(f"Página {page_idx + 1}: Nenhum retângulo detectado.")
            continue

        matricula_info = max(recortes_info, key=lambda r: r["w"] / r["h"])
        cutout_infos = [r for r in recortes_info if r != matricula_info]
        cutout_infos = sorted(cutout_infos, key=lambda r: r["x"])

        cutout_paths = []
        for idx, info in enumerate(cutout_infos):
            pts = ordenar_pontos(info["rect"])
            (tl, tr, br, bl) = pts
            widthA = np.linalg.norm(br - bl)
            widthB = np.linalg.norm(tr - tl)
            maxWidth = int(max(widthA, widthB))
            heightA = np.linalg.norm(tr - br)
            heightB = np.linalg.norm(tl - bl)
            maxHeight = int(max(heightA, heightB))

            destino = np.array([
                [0, 0],
                [maxWidth - 1, 0],
                [maxWidth - 1, maxHeight - 1],
                [0, maxHeight - 1]], dtype="float32")

            M = cv2.getPerspectiveTransform(pts, destino)
            warp = cv2.warpPerspective(img, M, (maxWidth, maxHeight))
            gray = cv2.cvtColor(warp, cv2.COLOR_BGR2GRAY)
            thresh = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY_INV)[1]
            path = os.path.join(cutouts_dir, f"page_{page_idx + 1}_column_{idx}.png")
            cv2.imwrite(path, thresh)
            cutout_paths.append(path)

        x, y, w, h = cv2.boundingRect(matricula_info["rect"])
        matricula_img = img[y:y + h, x:x + w]
        matricula_gray = cv2.cvtColor(matricula_img, cv2.COLOR_BGR2GRAY)
        matricula_thresh = cv2.threshold(matricula_gray, 170, 255, cv2.THRESH_BINARY_INV)[1]
        matricula_path = os.path.join(matricula_dir, f"matricula_{page_idx + 1}.png")
        cv2.imwrite(matricula_path, matricula_thresh)

        total_questions = 60
        options = 5
        cols = 4
        questions_per_col = total_questions // cols

        def detect_marked_choice(thresh_question):
            height, width = thresh_question.shape
            new_width = width - (width % options)
            thresh_question = thresh_question[:, :new_width]
            columns = np.hsplit(thresh_question, options)
            pixel_counts = [cv2.countNonZero(col) for col in columns]
            total_pixels = sum(pixel_counts)
            if total_pixels < 1000:
                return [0] * options
            max_count = max(pixel_counts)
            threshold = max_count * 0.6
            vector = [1 if count >= threshold else 0 for count in pixel_counts]
            if vector.count(1) != 1:
                return [0] * options
            return vector

        answers = []
        for col_idx, path in enumerate(cutout_paths):
            img_col = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
            if img_col is None:
                continue
            h, w = img_col.shape
            box_height = h // questions_per_col
            for i in range(questions_per_col):
                y1 = i * box_height
                y2 = (i + 1) * box_height
                question = img_col[y1:y2, 0:w]
                vector = detect_marked_choice(question)
                question_number = col_idx * questions_per_col + i + 1
                answers.append((question_number, vector))

        def detect_marked_matricula(thresh_matricula):
            height, width = thresh_matricula.shape
            num_digits = 8
            new_width = width - (width % num_digits)
            thresh_matricula = thresh_matricula[:, :new_width]
            columns = np.hsplit(thresh_matricula, num_digits)
            matricula_digits = []
            for col in columns:
                col_height = col.shape[0]
                adjusted_height = col_height - (col_height % 10)
                col = col[:adjusted_height, :]
                digit_rows = np.vsplit(col, 10)
                pixel_counts = [cv2.countNonZero(row) for row in digit_rows]
                max_count = max(pixel_counts)
                threshold = max_count * 0.6
                marked_indices = [i for i, count in enumerate(pixel_counts) if count >= threshold]
                if len(marked_indices) == 1:
                    matricula_digits.append(str(marked_indices[0]))
                else:
                    matricula_digits.append(None)
            return matricula_digits

        matricula_digits = detect_marked_matricula(matricula_thresh)
        matricula_str = "".join(d if d else "_" for d in matricula_digits)

        # Agrupando as respostas por página e coluna para estrutura JSON
        agrupamento_colunas = {}
        for (num, ans) in answers:
            coluna_index = (num - 1) // questions_per_col + 1
            if coluna_index not in agrupamento_colunas:
                agrupamento_colunas[coluna_index] = []
            resposta_formatada = ans if ans else "_"
            agrupamento_colunas[coluna_index].append({"questao": num, "resposta": resposta_formatada})

        #necessario o campo pagina para manter a contagem das paginas no json e csv
        for coluna, respostas in agrupamento_colunas.items():
            resultado.append({
                "pagina": page_idx + 1,
                "coluna": coluna,
                "matricula": matricula_str,
                "respostas": respostas
            })

    # Estrutura final do JSON
    json_structure = {
        "id": upload_id,
        "nome_do_arquivo": pdf_name,
        "resultado": resultado
    }

    result_json_path = os.path.join(json_dir, "graded_result.json")
    with open(result_json_path, "w", encoding="utf-8") as f_json:
        json.dump(json_structure, f_json, indent=4, ensure_ascii=False)

    # CSV ainda no formato simples (você pode adaptar se desejar)
    result_csv_path = os.path.join(json_dir, "graded_result.csv")
    with open(result_csv_path, "w", encoding="utf-8") as f_csv:
        f_csv.write("nome_do_arquivo;pagina;coluna;matricula;questao;A;B;C;D;E\n")
        for pagina_info in resultado:
            for resp in pagina_info["respostas"]:
                #antiga estrutura para pegar as paginas (funcional porém complexa em relação ao JSON a estrutura do servidor)
                a, b, c, d, e = resp["resposta"] if isinstance(resp["resposta"], list) else [0, 0, 0, 0, 0]
                f_csv.write(f"{pdf_name};{pagina_info['pagina']};{pagina_info['coluna']};{pagina_info['matricula']};{resp['questao']};{a};{b};{c};{d};{e}\n")

if __name__ == "__main__":
    # testar novos parametros de captura adicionados para saber se ele recebe parametro
    # se recebe deixar, se não recebe analisar
    upload_counter = 1
    for file in os.listdir(BASE_INPUT_DIR):
        if file.lower().endswith(".pdf"):
            full_path = os.path.join(BASE_INPUT_DIR, file)
            try:
                process_pdf(full_path, upload_id=upload_counter)
                upload_counter += 1
                processed_dir = os.path.join(BASE_INPUT_DIR, "processados")
                os.makedirs(processed_dir, exist_ok=True)
                shutil.move(full_path, os.path.join(processed_dir, file))
            except Exception as e:
                print(f"Erro ao processar {file}: {e}")