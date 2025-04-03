# def stackImages(imgArray, scale, lables=[]):
#     rows = len(imgArray)
#     cols = len(imgArray[0])
#     rowsAvailable = isinstance(imgArray[0], list)
#     width = imgArray[0][0].shape[1]
#     height = imgArray[0][0].shape[0]
#     if rowsAvailable:
#         for x in range (0, rows):
#             for y in range (0, cols):
#                 imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
#                 if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
#         imageBlank = np.zeros((height, width, 3), np.uint8)
#         hor = [imageBlank]*rows
#         hor_con = [imageBlank]*rows
#         for x in range(0, rows):
#             hor[x] = np.hstack(imgArray[x])
#             hor_con[x] = np.concatenate(imgArray[x])
#         ver = np.vstack(hor)
#         ver_con = np.concatenate(hor)
#     else:
#         for x in range(0, rows):
#             imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
#             if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
#         hor= np.hstack(imgArray)
#         hor_con= np.concatenate(imgArray)
#         ver = hor
#     if len(lables) != 0:
#         eachImgWidth = int(ver.shape[1] / cols)
#         eachImgHeight = int(ver.shape[0] / rows)
#         #print(eachImgHeight)
#         for d in range(0, rows):
#             for c in range (0,cols):
#                 cv2.rectangle(ver, (c*eachImgWidth, eachImgHeight*d), (c*eachImgWidth + len(lables[d][c])*13+27, 30+eachImgHeight*d), (255, 255, 255), cv2.FILLED)
#                 cv2.putText(ver, lables[d][c], (eachImgWidth*c+10, eachImgHeight*d+20), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 0, 255), 2)
#     return ver

# utils.py
import cv2
import numpy as np

def findRectContours(contours):
    """Finds rectangular contours in an image."""
    rectContours = []
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 50:
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            if len(approx) == 4:
                rectContours.append(cnt)
    rectContours = sorted(rectContours, key=cv2.contourArea, reverse=True)
    return rectContours

def getCornerPoints(contour):
    """Returns corner points of a contour."""
    peri = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.02 * peri, True)
    return approx

def reorder(points):
    """Reorders corner points to consistent format."""
    points = points.reshape((4, 2))
    new_points = np.zeros((4, 1, 2), np.int32)

    add = points.sum(1)
    diff = np.diff(points, axis=1)

    new_points[0] = points[np.argmin(add)]    # top-left
    new_points[3] = points[np.argmax(add)]    # bottom-right
    new_points[1] = points[np.argmin(diff)]   # top-right
    new_points[2] = points[np.argmax(diff)]   # bottom-left

    return new_points

def grade_answers(detected_answers, answer_key):
    """Compares detected answers to the official answer key."""
    result = {}
    correct = 0
    incorrect = 0

    for number, answer in detected_answers.items():
        if isinstance(number, int):
            correct_answer = answer_key.get(number)
            if answer is None:
                result[number] = {
                    "answer": None,
                    "correct_answer": correct_answer,
                    "status": "blank"
                }
            elif answer == correct_answer:
                result[number] = {
                    "answer": answer,
                    "correct_answer": correct_answer,
                    "status": "correct"
                }
                correct += 1
            else:
                result[number] = {
                    "answer": answer,
                    "correct_answer": correct_answer,
                    "status": "incorrect"
                }
                incorrect += 1

    total = correct + incorrect
    percent = round((correct / total) * 100, 2) if total > 0 else 0

    result["_summary"] = {
        "correct": correct,
        "incorrect": incorrect,
        "accuracy_percent": percent
    }

    return result
