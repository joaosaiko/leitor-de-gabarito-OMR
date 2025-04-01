import cv2
import numpy as np
import os
import utils  # Certifique-se de que utils.py está implementado corretamente
from pdf2image import convert_from_path

output_jpeg = "jpeg"
os.makedirs(output_jpeg, exist_ok=True)

#Converter PDF para JPEG
# Converter PDF para JPEG
pdf_path = "7.pdf"  # Substitua pelo nome do seu arquivo PDF
pages = convert_from_path(pdf_path, dpi=300)  # Converte todas as páginas em imagens

# Salvar a primeira página como JPEG
jpeg_path = os.path.join(output_jpeg, "pagina_1.jpeg")
pages[0].save(jpeg_path, "JPEG")

# Atualiza a variável path com o caminho da imagem JPEG gerada
path = jpeg_path
print(path)

# Configurações
widthImg = 3000
heightImg = 2600
questions = 60
choices = 5
columns = 4
questions_per_col = questions // columns  # 15 por coluna
output_folder = "recortes"
os.makedirs(output_folder, exist_ok=True)

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
        x, y, w, h = cv2.boundingRect(points)
        imgColuna = img[y:y+h, x:x+w]
        imgWarpGray = cv2.cvtColor(imgColuna, cv2.COLOR_BGR2GRAY)
        imgThresh = cv2.threshold(imgWarpGray, 160, 255, cv2.THRESH_BINARY_INV)[1]
        save_path = os.path.join(output_folder, f"coluna_{idx+1}.png")
        cv2.imwrite(save_path, imgThresh)
        colunas_paths.append(save_path)
        print(f"Salvo: {save_path}")

# Estrutura para identificar as respostas marcadas
def get_marked_choice(thresh_question):
    height, width = thresh_question.shape
    new_width = width - (width % choices)  # corta o excesso
    thresh_question = thresh_question[:, :new_width]  # faz crop da largura
    cols = np.hsplit(thresh_question, choices)
    pixel_counts = [cv2.countNonZero(col) for col in cols]
    print(pixel_counts)
    max_value = max(pixel_counts)
    if max_value < 800:
        return None
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

# Mostrar as respostas identificadas
print("\nRespostas Identificadas:")
for numero, resposta in respostas:
    print(f"Questão {numero:02d}: {resposta if resposta else 'Sem marcação'}")

#usado apenas para visualização (opcional)
# imgBlank = np.zeros_like(img)
# imageArray = ([img, imgGray, imgBlur, imgCanny],
#               [imgContours, imgBigContours, imgBlank, imgBlank])
# imgStacked = utils.stackImages(imageArray, 0.5)

# cv2.imshow("Stacked Images", imgStacked)

cv2.waitKey(0)
cv2.destroyAllWindows()