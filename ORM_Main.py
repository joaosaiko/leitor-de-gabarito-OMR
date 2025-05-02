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

# Mock answer key
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
    os.makedirs("jpeg", exist_ok=True)
    os.makedirs("json", exist_ok=True)
    os.makedirs("cutouts", exist_ok=True)
    os.makedirs("matricula", exist_ok=True)

    with NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    pages = convert_from_path(tmp_path, dpi=300)
    jpeg_path = os.path.join("jpeg", "page_1.jpeg")
    pages[0].save(jpeg_path, "JPEG")

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

    recortes_info = []
    for rect in rectangles:
        x, y, w, h = cv2.boundingRect(rect)
        recortes_info.append({"x": x, "y": y, "w": w, "h": h, "rect": rect})

    recortes_info = sorted(recortes_info, key=lambda r: (r["y"], -r["w"]))
    matricula_info = max(recortes_info, key=lambda r: r["w"] / r["h"])
    cutout_infos = [r for r in recortes_info if r != matricula_info]
    cutout_infos = sorted(cutout_infos, key=lambda r: r["x"])


    cutout_paths = []
    for idx, info in enumerate(cutout_infos):
        x, y, w, h = cv2.boundingRect(info["rect"])
        crop = img[y:y+h, x:x+w]
        gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY_INV)[1]
        path = os.path.join("cutouts", f"column_{idx}.png")
        cv2.imwrite(path, thresh)
        cutout_paths.append(path)

    x, y, w, h = cv2.boundingRect(matricula_info["rect"])
    matricula_img = img[y:y+h, x:x+w]
    matricula_gray = cv2.cvtColor(matricula_img, cv2.COLOR_BGR2GRAY)
    matricula_thresh = cv2.threshold(matricula_gray, 180, 255, cv2.THRESH_BINARY_INV)[1]
    matricula_path = os.path.join("matricula", "matricula.png")
    cv2.imwrite(matricula_path, matricula_thresh)

    total_questions = 60 # total de questoes
    options = 5 # numero de opcoes
    cols = 4 # numero de colunas
    questions_per_col = total_questions // cols # questoes por coluna

    def detect_marked_choice(thresh_question):
        height, width = thresh_question.shape
        new_width = width - (width % options)
        thresh_question = thresh_question[:, :new_width]
        columns = np.hsplit(thresh_question, options)
        pixel_counts = [cv2.countNonZero(col) for col in columns]
        print("Pixel counts:", pixel_counts)
        threshold = 2000 # qualquer problema com as repostas sendo identificadas como null, modificar esse trecho
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

    matricula_digits = detect_marked_matricula(matricula_thresh)
    print("Matricula encontrada:", "".join(d if d else "_" for d in matricula_digits))

    detected = {}
    detected["_matricula"] = {
        "digits": matricula_digits,
        "as_string": "".join(d if d else "_" for d in matricula_digits)
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
