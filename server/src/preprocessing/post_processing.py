'''
Doc
'''


import cv2
from PIL import Image
import pytesseract
from preprocessing import Preprocessing

class Post_Processing:
    '''Doc'''


    def __init__(self, text):
        self.text = text
    
    @staticmethod
    def check_receipt_angle(text):
        return "Արարատ Սուպերմարկետ" in text.split("\n")
    
    @staticmethod
    def rotate_image_90(image_path):
        image = cv2.imread(image_path)
        rotated_image = cv2.transpose(image)
        rotated_image = cv2.flip(rotated_image, 0)
        cv2.imwrite(image_path, rotated_image)
    
    def post_process(self):
        RESULT_IMAGE_PATH = "./src/images/result.png"
        for _ in range(3):
            if self.check_receipt_angle(self.text):
                return self.text
            self.rotate_image_90(RESULT_IMAGE_PATH)
            img = Image.open(RESULT_IMAGE_PATH)
            self.text = pytesseract.image_to_string(img, lang="Armenian+rus")
        return ''

preprocessor = Preprocessing("./src/images/7.jpg")
result_text = preprocessor.process_image()
post = Post_Processing(result_text)
print(post.post_process())
