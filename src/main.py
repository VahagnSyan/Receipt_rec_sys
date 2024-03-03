from PIL import Image
import pytesseract

image_path = "./src/images/1.png"

img = Image.open(image_path)

text = pytesseract.image_to_string(img, lang="Armenian")

print(text)
