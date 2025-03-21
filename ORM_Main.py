#OMRmain.py
import cv2
import numpy as np
import os
import utils  # Certifique-se de que utils.py está implementado corretamente

# Carregar imagem
path = "imagens_bases/2.jpg"
widthImg = 700
heightImg = 800
img = cv2.imread(path)
img = cv2.resize(img, (widthImg, heightImg))

# Criar pasta para armazenar os recortes
output_folder = "recortes"
os.makedirs(output_folder, exist_ok=True)

# Pré-processamento
imgContours = img.copy()
imgBigContours = img.copy()
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)
imgCanny = cv2.Canny(imgBlur, 10, 50)

# Encontrar contornos
contours, _ = cv2.findContours(imgCanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(imgContours, contours, -1, (0, 255, 0), 2)
rectCon = utils.rectCountour(contours)

if len(rectCon) >= 4:
    gradePoints = [utils.getCornerPoints(rectCon[i]) for i in range(4)]
    gradePoints = [utils.reorder(pts) for pts in gradePoints]
    
    # Ordenar colunas da esquerda para a direita com base na coordenada x mínima
    gradePoints.sort(key=lambda pts: np.min(pts[:, 0]))
    
    for idx, points in enumerate(gradePoints):
        cv2.drawContours(imgBigContours, points, -1, (0, 255, 0), 20)
        
        # Obter retângulo delimitador
        x, y, w, h = cv2.boundingRect(points)
        imgColuna = img[y:y+h, x:x+w]  # Recortar diretamente a área delimitada
        
        # Aplicar threshold para inverter cores e destacar marcações
        imgWarpGray = cv2.cvtColor(imgColuna, cv2.COLOR_BGR2GRAY)
        imgThresh = cv2.threshold(imgWarpGray, 150, 255, cv2.THRESH_BINARY_INV)[1]
        
        # Salvar a imagem processada
        save_path = os.path.join(output_folder, f"coluna_{idx+1}.png")
        cv2.imwrite(save_path, imgThresh)
        print(f"Salvo: {save_path}")

# Criar imagens empilhadas para visualização
imgBlank = np.zeros_like(img)
imageArray = ([img, imgGray, imgBlur, imgCanny],
              [imgContours, imgBigContours, imgBlank, imgBlank])
imgStacked = utils.stackImages(imageArray, 0.5)

cv2.imshow("Stacked Images", imgStacked)
cv2.waitKey(0)
cv2.destroyAllWindows()
