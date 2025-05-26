from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import cv2
import numpy as np
import os
from pdf2image import convert_from_path
import json
from tempfile import NamedTemporaryFile
import uuid
import threading
import time

app = FastAPI(
    title="PROINT",
    description="Sistema de correção de provas de múltipla escolha com visão computacional",
    version="1.0.0",
)

@app.get("/")
async def root():
    return {"message": "API PROINT está rodando!"}

@app.post("/process-pdf")
async def process_pdf(file: UploadFile = File(...)):
    session_id = str(uuid.uuid4())
    base_dir = os.path.join("temp", session_id)
    jpeg_dir = os.path.join(base_dir, "jpeg")
    cutouts_dir = os.path.join(base_dir, "cutouts")
    json_dir = os.path.join(base_dir, "json")
    matricula_dir = os.path.join(base_dir, "matricula")

    for d in [jpeg_dir, cutouts_dir, json_dir, matricula_dir]:
        os.makedirs(d, exist_ok=True)

    try:
        with NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(await file.read())
            tmp_path = tmp.name

        pages = convert_from_path(tmp_path, dpi=300)
        pdf_name = file.filename
        linhas = []

        for page_idx, page in enumerate(pages):
            jpeg_path = os.path.join(jpeg_dir, f"page_{page_idx + 1}.jpeg")
            page.save(jpeg_path, "JPEG")

            img = cv2.imread(jpeg_path)
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
            matricula_img = img[y:y+h, x:x+w]
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
                max_count = max(pixel_counts)
                threshold = max_count * 0.6
                marked_indices = [i for i, count in enumerate(pixel_counts) if count >= threshold]
                if len(marked_indices) == 1:
                    return chr(65 + marked_indices[0])
                return None

            answers = []
            for col_idx, path in enumerate(cutout_paths):
                img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
                h, w = img.shape
                box_height = h // questions_per_col
                for i in range(questions_per_col):
                    y1 = i * box_height
                    y2 = (i + 1) * box_height
                    question = img[y1:y2, 0:w]
                    choice = detect_marked_choice(question)
                    question_number = col_idx * questions_per_col + i + 1
                    answers.append((question_number, choice))

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

            for idx, (num, ans) in enumerate(answers):
                coluna_index = (num - 1) // questions_per_col + 1
                alternativa_marcada = ["0"] * options
                if ans:
                    alternativa_idx = ord(ans.upper()) - 65
                    if 0 <= alternativa_idx < options:
                        alternativa_marcada[alternativa_idx] = "1"
                resposta_formatada = "-".join(alternativa_marcada)
                linha = f"{pdf_name}, page_{page_idx + 1}, column_{coluna_index}, {matricula_str}, {resposta_formatada}"
                linhas.append(linha)

        result_json_path = os.path.join(json_dir, "graded_result.json")
        with open(result_json_path, "w") as f_json:
            json.dump({"linhas": linhas}, f_json, indent=4)

        result_csv_path = os.path.join(json_dir, "graded_result.csv")
        with open(result_csv_path, "w", encoding="utf-8") as f_csv:
            f_csv.write("nome_do_arquivo;pagina;coluna;matricula;resposta\n")
            for linha in linhas:
                partes = linha.split(", ")
                f_csv.write(";".join(partes) + "\n")

        def remove_folder_later():
            time.sleep(1800)
            import shutil
            shutil.rmtree(base_dir, ignore_errors=True)

        threading.Thread(target=remove_folder_later, daemon=True).start()

        return {
            "resultado_linhas": linhas,
            "session_id": session_id,
            "mensagem": "Resultado disponível por 30 minutos",
        }

    except Exception as e:
        return JSONResponse(status_code=500, content={"erro": str(e)})
