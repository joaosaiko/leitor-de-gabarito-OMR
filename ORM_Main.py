#OMR_MAIN.py
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
    6: 'D',  7: 'C',  8: 'B',  9: 'C', 10: 'D',
    11: 'E', 12: 'D', 13: 'C', 14: None, 15: None,
    16: 'A', 17: 'A', 18: 'A', 19: 'A', 20: 'A',
    21: 'A', 22: 'B', 23: 'B', 24: 'B', 25: 'B',
    26: 'B', 27: 'B', 28: 'C', 29: 'C', 30: 'C',
    31: 'A', 32: 'C', 33: 'B', 34: 'C', 35: 'D',
    36: 'E', 37: 'D', 38: 'C', 39: 'B', 40: 'A',
    41: 'B', 42: 'D', 43: 'E', 44: 'C', 45: 'B',
    46: 'C', 47: 'C', 48: 'C', 49: 'E', 50: 'D',
    51: 'E', 52: 'E', 53: 'E', 54: None, 55: 'D',
    56: 'D', 57: 'D', 58: 'C', 59: 'A', 60: 'E'
}

@app.post("/process-pdf")
async def process_pdf(file: UploadFile = File(...)):
    # Output folders
    os.makedirs("jpeg", exist_ok=True)
    os.makedirs("json", exist_ok=True)
    os.makedirs("cutouts", exist_ok=True)

    # Save uploaded PDF
    with NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    # Convert PDF to image
    pages = convert_from_path(tmp_path, dpi=300)
    jpeg_path = os.path.join("jpeg", "page_1.jpeg")
    pages[0].save(jpeg_path, "JPEG")

    image_path = jpeg_path
    width, height = 3000, 2600
    total_questions = 60
    options = 5
    cols = 4
    questions_per_col = total_questions // cols

    img = cv2.imread(image_path)
    img = cv2.resize(img, (width, height))

    # Preprocess
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, (5, 5), 1)
    img_canny = cv2.Canny(img_blur, 10, 50)

    contours, _ = cv2.findContours(img_canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    rects = utils.findRectContours(contours)

    cutout_paths = []
    if len(rects) >= 4:
        points = [utils.getCornerPoints(rects[i]) for i in range(4)]
        points = [utils.reorder(p) for p in points]
        points.sort(key=lambda p: np.min(p[:, 0]))

        for idx, pts in enumerate(points):
            x, y, w, h = cv2.boundingRect(pts)
            col_img = img[y:y+h, x:x+w]
            gray = cv2.cvtColor(col_img, cv2.COLOR_BGR2GRAY)
            thresh = cv2.threshold(gray, 160, 255, cv2.THRESH_BINARY_INV)[1]
            path = os.path.join("cutouts", f"column_{idx+1}.png")
            cv2.imwrite(path, thresh)
            cutout_paths.append(path)

    def detect_marked_choice(thresh_question):
        height, width = thresh_question.shape
        new_width = width - (width % options)
        thresh_question = thresh_question[:, :new_width]
        columns = np.hsplit(thresh_question, options)
        pixel_counts = [cv2.countNonZero(col) for col in columns]
        print(pixel_counts)

        # Considera apenas colunas com preenchimento acima do limiar
        threshold = 900
        marked_indices = [i for i, count in enumerate(pixel_counts) if count > threshold]

        # Se mais de uma alternativa marcada, invalida a resposta
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

    detected = {}
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
