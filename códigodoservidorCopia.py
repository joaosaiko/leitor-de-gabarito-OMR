import cv2
import numpy as np
import os
from pdf2image import convert_from_path
import json
import shutil
from datetime import datetime
import sys
from pathlib import Path


# Diretórios fixos no disco
BASE_INPUT_DIR = r"C:\appprointer\app\data\PDF"
BASE_OUTPUT_DIR = r"C:\appprointer\app\data\Processados"


# Cria diretórios se não existirem
os.makedirs(BASE_INPUT_DIR, exist_ok=True)
os.makedirs(BASE_OUTPUT_DIR, exist_ok=True)

def sanitize_filename(filename):
    return "".join(c if c.isalnum() or c in [' ', '_', '-'] else "_" for c in filename)

def process_pdf(input_pdf_path, upload_id=1):
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

    #print(f"Convertendo PDF em imagens: {input_pdf_path}")
    pages = convert_from_path(input_pdf_path, dpi=300)

    resultado = []

    for page_idx, page in enumerate(pages):
        jpeg_path = os.path.join(jpeg_dir, f"page_{page_idx + 1}.jpeg")
        page.save(jpeg_path, "JPEG")

        img = cv2.imread(jpeg_path)
        if img is None:
            print(f"Erro: Não foi possível ler a imagem salva em {jpeg_path}")
            continue

            top, second = candidates[0], candidates[1]
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)) # Em casos de não identificação das colunas mudar o kernel para operações morfológicas
        morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel) # Aplica fechamento morfológico
        canny = cv2.Canny(morph, 70, 130) # Ajuste os valores de limiar conforme necessário

        contours, _ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # Encontra os contornos na imagem
        rectangles = []
        for cnt in contours:
            area = cv2.contourArea(cnt) # Calcula a área do contorno
            if area > 2000:
                peri = cv2.arcLength(cnt, True) 
                approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
                if len(approx) == 4:
                    rectangles.append(approx)
        
                # Salva imagem com retângulos detectados
                img_rects = img.copy()
                cv2.drawContours(img_rects, rectangles, -1, (0, 255, 0), 3)
                rects_img_path = os.path.join("C:/Users/estagiario.inovacao/Desktop/leitor-de-gabarito-OMR/retangulos_detect", f"page_{page_idx + 1}_rectangles.jpeg")
                cv2.imwrite(rects_img_path, img_rects)
       
        def ordenar_pontos(pontos):
            pontos = pontos.reshape(4, 2)
            soma = pontos.sum(axis=1)
            diff = np.diff(pontos, axis=1)
            ordenado = np.zeros((4, 2), dtype="float32")
            ordenado[0] = pontos[np.argmin(soma)] # Ponto superior esquerdo
            ordenado[1] = pontos[np.argmin(diff)] # Ponto superior direito
            ordenado[2] = pontos[np.argmax(soma)] # Ponto inferior direito
            ordenado[3] = pontos[np.argmax(diff)] # Ponto inferior esquerdo
                        
            return ordenado

        recortes_info = []
        for rect in rectangles:
            x, y, w, h = cv2.boundingRect(rect)
            recortes_info.append({"x": x, "y": y, "w": w, "h": h, "rect": rect})

        recortes_info = sorted(recortes_info, key=lambda r: (r["y"], -r["w"]))
        if not recortes_info:
            #print(f"Página {page_idx + 1}: Nenhum retângulo detectado.")
            continue

        matricula_info = max(recortes_info, key=lambda r: r["w"] * r["h"])

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

        #funcao para detectar o vetor de escolhas marcadas
        def detect_marked_choice_vector(thresh_question):
            height, width = thresh_question.shape
            new_width = width - (width % options)
            thresh_question = thresh_question[:, :new_width]
            columns = np.hsplit(thresh_question, options)
            pixel_counts = [cv2.countNonZero(col) for col in columns]
            
            total_pixels = sum(pixel_counts)
            # estrutura de decisão para evitar processamento desnecessário
            if total_pixels < 800: # valor padrao 800 
                return [0] * options

            max_count = max(pixel_counts)
            threshold = max_count * 0.5 # 50% melhor valor, menos que isso gera ruído
            
            vector = [1 if count >= threshold else 0 for count in pixel_counts]
            
            if vector.count(1) > 2:
                return [0] * options

            return vector

        answers = []
        for col_idx, path in enumerate(cutout_paths):
            img_col = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
            if img_col is None:
                print(f"Erro ao ler corte {path}")
                continue
            h, w = img_col.shape
            box_height = h // questions_per_col
            for i in range(questions_per_col):
                y1 = i * box_height
                y2 = (i + 1) * box_height
                question = img_col[y1:y2, 0:w]
                vector = detect_marked_choice_vector(question)
                question_number = col_idx * questions_per_col + i + 1
                answers.append((question_number, vector))

        # funcao para detectar a matrícula
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
                
                # Filtra os valores que são maiores que 1500
                valid_pixel_counts = [count for count in pixel_counts if count > 1500]
                
                # Se houver valores válidos, seleciona o máximo
                if valid_pixel_counts:
                    max_count = max(valid_pixel_counts)
                else:
                    max_count = 0  # ou outro valor de fallback se nenhum valor válido for encontrado
                
                threshold = max_count * 0.7  # 70% do valor máximo como limite
                marked_indices = [i for i, count in enumerate(pixel_counts) if count >= threshold]
                
                if len(marked_indices) == 1:
                    matricula_digits.append(str(marked_indices[0]))
                else:
                    matricula_digits.append(None)
            
            return matricula_digits

        matricula_digits = detect_marked_matricula(matricula_thresh)
        matricula_str = "".join(d if d else "_" for d in matricula_digits)

        agrupamento_colunas = {}
        for (num, vec) in answers:
            coluna_index = (num - 1) // questions_per_col + 1
            if coluna_index not in agrupamento_colunas:
                agrupamento_colunas[coluna_index] = []
            agrupamento_colunas[coluna_index].append({
                "questao": num,
                "resposta_vetorial": vec
            })

        for coluna, respostas in agrupamento_colunas.items():
            resultado.append({
                "pagina": page_idx + 1,
                "coluna": coluna,
                "matricula": matricula_str,
                "respostas": respostas
            })

    json_structure = {
        "id": upload_id,
        "nome_do_arquivo": pdf_name,
        "resultado": resultado
    }

    result_json_path = os.path.join(json_dir, "graded_result.json")
    with open(result_json_path, "w", encoding="utf-8") as f_json:
        json.dump(json_structure, f_json, indent=4, ensure_ascii=False)

    result_csv_path = os.path.join(json_dir, "graded_result.csv")
    with open(result_csv_path, "w", encoding="utf-8") as f_csv:
        f_csv.write("Id_Gabarito;Arquivo;MATRICULA;QUESTAO;A;B;C;D;E\n")
        print("Id_Gabarito;Arquivo;MATRICULA;QUESTAO;A;B;C;D;E")
        for pagina_info in resultado:
            pag = pagina_info["pagina"]
            for resp in pagina_info["respostas"]:
                linha_csv = f"{gabarito_id};{nome_arquivo}_page_{pag};{pagina_info['matricula']};{resp['questao']};" + ";".join(str(x) for x in resp['resposta_vetorial'])
                f_csv.write(linha_csv + "\n")
                print(linha_csv)

    #print(f"✔ Processamento concluído! Resultados salvos em: {json_dir}")

if __name__ == "__main__":
    upload_counter = 1
    gabarito_id = sys.argv[1]
    nome_arquivo = Path(sys.argv[2]).stem
    #gabarito_id = 0
    #print(gabarito_id)
    #print(nome_arquivo)


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