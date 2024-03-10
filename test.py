from PIL import Image
from rembg import remove 
import pytesseract

pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

image_path = '/home/vahag/Downloads/1.png'  # Replace with your image path
img = Image.open(image_path)
output = remove(img)
output.save('output.png')


text = pytesseract.image_to_string(img, lang="Armenian")

print(text)