# OMR_Main.py
import cv2
import numpy as np
import os
import utils
from pdf2image import convert_from_path
import json

# Criar pastas de saída
output_jpeg = "jpeg"
os.makedirs("jpeg", exist_ok=True)

output_json = "json"
os.makedirs("json", exist_ok=True)

output_cutout = "recortes"
os.makedirs(output_cutout, exist_ok=True)

# Converter PDF para JPEG
pdf_path = "9.pdf"  # Substitua pelo nome do seu arquivo PDF
pages = convert_from_path(pdf_path, dpi=300)  # Converte todas as páginas em imagens

# Salvar a primeira página como JPEG
jpeg_path = os.path.join(output_jpeg, "pagina_1.jpeg")
pages[0].save(jpeg_path, "JPEG")

# Atualiza a variável path com o caminho da imagem JPEG gerada
path = jpeg_path

# Configurações
widthImg = 3000
heightImg = 2600
questions = 60
choices = 5
columns = 4
questions_per_col = questions // columns  # 15 por coluna

# Carregar e redimensionar imagem
img = cv2.imread(path)
img = cv2.resize(img, (widthImg, heightImg))

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

# Processar colunas
colunas_paths = []
if len(rectCon) >= 4:
    gradePoints = [utils.getCornerPoints(rectCon[i]) for i in range(4)]
    gradePoints = [utils.reorder(pts) for pts in gradePoints]
    gradePoints.sort(key=lambda pts: np.min(pts[:, 0]))

    for idx, points in enumerate(gradePoints):
        cv2.drawContours(imgBigContours, points, -1, (0, 255, 0), 20)
        x, y, w, h = cv2.boundingRect(points) # recorta a coluna
        imgColuna = img[y:y+h, x:x+w] # recorta a coluna
        imgWarpGray = cv2.cvtColor(imgColuna, cv2.COLOR_BGR2GRAY)  
        imgThresh = cv2.threshold(imgWarpGray, 160, 255, cv2.THRESH_BINARY_INV)[1] 
        save_path = os.path.join(output_cutout, f"coluna_{idx+1}.png")
        cv2.imwrite(save_path, imgThresh)
        colunas_paths.append(save_path)
        print(f"Salvo: {save_path}")

def get_marked_choice(thresh_question):
    '''Identifica a resposta marcada em uma questão de múltipla escolha.'''

    height, width = thresh_question.shape
    new_width = width - (width % choices)  # corta o excesso
    thresh_question = thresh_question[:, :new_width]  # faz crop da largura
    cols = np.hsplit(thresh_question, choices)
    pixel_counts = [cv2.countNonZero(col) for col in cols]
    print(pixel_counts)
    max_value = max(pixel_counts)
    if max_value < 800: return None
    return chr(65 + pixel_counts.index(max_value))

respostas = []
for idx_coluna, path_coluna in enumerate(colunas_paths):
    img = cv2.imread(path_coluna, cv2.IMREAD_GRAYSCALE)
    h, w = img.shape
    box_height = h // questions_per_col
    for i in range(questions_per_col):
        y1 = i * box_height
        y2 = (i + 1) * box_height
        questao = img[y1:y2, 0:w]
        resposta = get_marked_choice(questao)
        numero_questao = idx_coluna * questions_per_col + i + 1
        respostas.append((numero_questao, resposta))

# guardar respostas identificadas em um arquivo json na pasta json
caminho = {}
resposta_ident, resposta_null = 0, 0
for num, resposta in respostas:
    if resposta:
        resposta_ident += 1
    else:
        resposta_null += 1
    caminho[num] = resposta

# adiciona contagens ao dicionário
caminho["_resumo"] = {
    "respostas_identificadas": resposta_ident,
    "respostas_nulas": resposta_null
}

with open(os.path.join(output_json, "respostas.json"), "w") as json_file:
    json.dump(caminho, json_file, indent=4)

#print("\nRespostas Identificadas:")
#for numero, resposta in respostas:
#    print(f"Questão {numero:02d}: {resposta if resposta else 'Sem marcação'}")

#usado apenas para visualização (opcional)
escala = 0.3  # ou 0.3, 0.25, etc. conforme preferir

#cv2.imshow("Tons de Cinza", cv2.resize(imgGray, (0, 0), fx=escala, fy=escala))
#cv2.imshow("Borrada", cv2.resize(imgBlur, (0, 0), fx=escala, fy=escala))
#cv2.imshow("threshould", cv2.resize(imgCanny, (0, 0), fx=escala, fy=escala))
cv2.imshow("Contorno canny", cv2.resize(imgContours, (0, 0), fx=escala, fy=escala))
cv2.imshow("Contornos vertices", cv2.resize(imgBigContours, (0, 0), fx=escala, fy=escala))

cv2.waitKey(0)
cv2.destroyAllWindows()