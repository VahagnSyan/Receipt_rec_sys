from PIL import Image
import pytesseract
from db.connect_db import connect_db

image_path = "./src/images/1.png"

img = Image.open(image_path)

text = pytesseract.image_to_string(img, lang="Armenian+rus")

print(text)

# connect_db()
