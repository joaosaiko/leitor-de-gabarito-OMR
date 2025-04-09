# Apenas para corverter a imagem para PDF para ser utilizada no OMR
import aspose.words as aw

doc = aw.Document()
builder = aw.DocumentBuilder(doc)

builder.insert_image("files_gab_test/completo.jpg")

doc.save("Gabarito Completo Marcado.pdf")