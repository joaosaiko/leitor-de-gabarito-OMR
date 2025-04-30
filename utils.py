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
    blank = 0

    for number, answer in detected_answers.items():
        if isinstance(number, int):
            correct_answer = answer_key.get(number)
            if answer is None:
                result[number] = {
                    "answer": None,
                    "correct_answer": correct_answer,
                    "status": "blank"
                }
                blank += 1
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

    total = correct + incorrect + blank
    percent = round((correct / total) * 100, 2) if total > 0 else 0

    result["_summary"] = {
        "correct": correct,
        "incorrect": incorrect,
        "blank": blank,
        "accuracy_percent": percent
    }

    return result