"""
Module for post-processing of text extracted from images.
"""


import cv2
from PIL import Image
import pytesseract


class PostProcessing:
    """
    Class for post-processing of text extracted from images.
    """

    def __init__(self, text):
        """
        Initialize the Post_Processing object.

        Args:
            text (str): The extracted text to be post-processed.
        """
        self.text = text

    @staticmethod
    def check_receipt_angle(text):
        """
        Check if the receipt angle is correct based on extracted text.

        Args:
            text (str): The extracted text from the image.

        Returns:
            bool: True if the receipt angle is correct, False otherwise.
        """
        return "Արարատ Սուպերմարկետ" in text.split("\n")

    @staticmethod
    def rotate_image_90(image_path):
        """
        Rotate the image by 90 degrees.

        Args:
            image_path (str): The path to the image to be rotated.
        """
        image = cv2.imread(image_path)
        rotated_image = cv2.transpose(image)
        rotated_image = cv2.flip(rotated_image, 0)
        cv2.imwrite(image_path, rotated_image)

    def post_process(self):
        """
        Perform post-processing of the extracted text.

        This method rotates the image if the receipt angle is incorrect,
        performs OCR on the rotated image, and repeats the process up to three times.

        Returns:
            str: The post-processed text.
        """
        result_image_path = "./src/images/result.png"
        for _ in range(3):
            if self.check_receipt_angle(self.text):
                return self.text
            self.rotate_image_90(result_image_path)
            img = Image.open(result_image_path)
            self.text = pytesseract.image_to_string(img, lang="Armenian+rus")
        return ''
