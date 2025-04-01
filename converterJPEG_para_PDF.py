import aspose.words as aw

doc = aw.Document()
builder = aw.DocumentBuilder(doc)

builder.insert_image("9.jpg")

doc.save("9.pdf")