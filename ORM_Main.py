from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import cv2
import numpy as np
import os
import utils
from pdf2image import convert_from_path
import json
from tempfile import NamedTemporaryFile

app = FastAPI()

# Mock answer key for 60 questions (A, B, C, D, E repeating)
answer_key = {
    1: 'A',  2: 'B',  3: 'C',  4: 'D',  5: 'E',
    6: 'D',  7: 'C',  8: 'B',  9: 'A', 10: 'B',
    11: 'C', 12: 'D', 13: 'E', 14: 'D', 15: 'C',
    16: 'A', 17: 'A', 18: 'A', 19: 'B', 20: 'B',
    21: 'B', 22: 'B', 23: 'C', 24: 'C', 25: 'C',
    26: 'C', 27: 'C', 28: 'D', 29: 'D', 30: 'D',
    31: 'A', 32: 'C', 33: 'D', 34: 'E', 35: 'D',
    36: 'C', 37: 'B', 38: 'E', 39: 'A', 40: 'E',
    41: 'C', 42: 'B', 43: 'A', 44: 'B', 45: 'C',
    46: 'E', 47: 'D', 48: 'A', 49: 'A', 50: 'A',
    51: 'B', 52: 'B', 53: 'C', 54: 'C', 55: 'C',
    56: 'D', 57: 'D', 58: 'E', 59: 'D', 60: 'C'
}

@app.post("/process-pdf")
async def process_pdf(file: UploadFile = File(...)):
    from tempfile import NamedTemporaryFile

    os.makedirs("jpeg", exist_ok=True)
    os.makedirs("json", exist_ok=True)
    os.makedirs("cutouts", exist_ok=True)
    os.makedirs("matricula", exist_ok=True)

    # Salvar PDF temporário
    with NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    # Converter para imagem
    pages = convert_from_path(tmp_path, dpi=300)
    jpeg_path = os.path.join("jpeg", "page_1.jpeg")
    pages[0].save(jpeg_path, "JPEG")

    img = cv2.imread(jpeg_path)
    #resized_img = cv2.resize(img, (1300, 1700)) tirei o resize para manter a proporção original e está funcionando melhor do que antes
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

    rectangles = sorted(rectangles, key=lambda cnt: np.min(cnt[:, 0]))

    cutout_paths = []
    matricula_path = None

    for idx, rect in enumerate(rectangles):
        x, y, w, h = cv2.boundingRect(rect)
        crop = img[y:y+h, x:x+w]

        if idx == 2:
            # Matrícula
            matricula_img = crop
            matricula_gray = cv2.cvtColor(matricula_img, cv2.COLOR_BGR2GRAY)
            matricula_thresh = cv2.threshold(matricula_gray, 180, 255, cv2.THRESH_BINARY_INV)[1]
            matricula_path = os.path.join("matricula", "matricula.png")
            cv2.imwrite(matricula_path, matricula_thresh)
        else:
            # Colunas de respostas
            col_img = crop
            gray = cv2.cvtColor(col_img, cv2.COLOR_BGR2GRAY)
            thresh = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY_INV)[1]
            path = os.path.join("cutouts", f"column_{idx}.png")
            cv2.imwrite(path, thresh)
            cutout_paths.append(path)

    # --- Mesma lógica anterior para leitura de respostas ---
    total_questions = 60
    options = 5
    cols = 4 # Número de colunas de respostas
    questions_per_col = total_questions // cols

    def detect_marked_choice(thresh_question):
        height, width = thresh_question.shape
        new_width = width - (width % options)
        thresh_question = thresh_question[:, :new_width]
        columns = np.hsplit(thresh_question, options)
        pixel_counts = [cv2.countNonZero(col) for col in columns]
        print("Pixel counts:", pixel_counts)
        threshold = 1500
        marked_indices = [i for i, count in enumerate(pixel_counts) if count > threshold]
        if len(marked_indices) != 1:
            return None
        return chr(65 + marked_indices[0])

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
            max_index = np.argmax(pixel_counts)
            if pixel_counts[max_index] > 1500:
                matricula_digits.append(str(max_index))
            else:
                matricula_digits.append(None)
        return matricula_digits

    # Print the detected matricula
    print("Matricula encontrada:", "".join(digit if digit else "_" for digit in detect_marked_matricula(matricula_thresh)))

    detected = {}
    matricula_thresh = cv2.imread(matricula_path, cv2.IMREAD_GRAYSCALE)
    matricula_digits = detect_marked_matricula(matricula_thresh)

    detected["_matricula"] = {
        "digits": matricula_digits,
        "as_string": "".join(digit if digit else "_" for digit in matricula_digits)
    }

    filled, blank = 0, 0
    for num, ans in answers:
        if ans:
            filled += 1
        else:
            blank += 1
        detected[num] = ans

    detected["_summary"] = {
        "marked_answers": filled,
        "blank_answers": blank
    }

    with open(os.path.join("json", "answers.json"), "w") as f:
        json.dump(detected, f, indent=4)

    graded_result = utils.grade_answers(detected, answer_key)

    with open(os.path.join("json", "graded_result.json"), "w") as f:
        json.dump(graded_result, f, indent=4)

    return JSONResponse(content=graded_result)
