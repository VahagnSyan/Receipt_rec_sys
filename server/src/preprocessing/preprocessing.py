"""
Module for picture preprocessing.

This module provides functionality for preprocessing images before text extraction.
"""


from PIL import Image
import pytesseract
import numpy as np
import cv2
import matplotlib.pyplot as plt


class Preprocessing:
    """
    Class for preprocessing images.
    """

    def __init__(self, file_name):
        """
        Initialize the Preprocessing object.

        Args:
            file_name (str): The path to the image file.
        """
        self.file_name = file_name

    @staticmethod
    def opencv_resize(image, ratio):
        """
        Resize an image using OpenCV.

        Args:
            image (numpy.ndarray): The image array.
            ratio (float): The ratio by which to resize the image.

        Returns:
            numpy.ndarray: The resized image.
        """
        width = int(image.shape[1] * ratio)
        height = int(image.shape[0] * ratio)
        dim = (width, height)
        return cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

    @staticmethod
    def plot_rgb(image):
        """
        Plot an RGB image using matplotlib.

        Args:
            image (numpy.ndarray): The RGB image array.
        """
        plt.figure(figsize=(16, 10))
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    @staticmethod
    def plot_gray(image):
        """
        Plot a grayscale image using matplotlib.

        Args:
            image (numpy.ndarray): The grayscale image array.
        """
        plt.figure(figsize=(16, 10))
        plt.imshow(image, cmap="Greys_r")

    @staticmethod
    def approximate_contour(contour):
        """
        Approximate a contour to reduce the number of points.

        Args:
            contour (numpy.ndarray): The contour array.

        Returns:
            numpy.ndarray: The approximated contour array.
        """
        peri = cv2.arcLength(contour, True)
        return cv2.approxPolyDP(contour, 0.032 * peri, True)

    @staticmethod
    def get_receipt_contour(contours):
        """
        Get the contour of the receipt.

        Args:
            contours (list): List of contours.

        Returns:
            numpy.ndarray: The contour of the receipt.
        """
        for c in contours:
            approx = Preprocessing.approximate_contour(c)
            if len(approx) == 4:
                return approx
        return None

    @staticmethod
    def contour_to_rect(contour, resize_ratio):
        """
        Convert a contour to rectangle coordinates.

        Args:
            contour (numpy.ndarray): The contour array.
            resize_ratio (float): The resize ratio used for resizing the image.

        Returns:
            numpy.ndarray: The rectangle coordinates.
        """
        pts = contour.reshape(4, 2)
        rect = np.zeros((4, 2), dtype="float32")
        s = pts.sum(axis=1)
        rect[0] = pts[np.argmin(s)]
        rect[2] = pts[np.argmax(s)]
        diff = np.diff(pts, axis=1)
        rect[1] = pts[np.argmin(diff)]
        rect[3] = pts[np.argmax(diff)]
        return rect / resize_ratio

    @staticmethod
    def wrap_perspective(img, rect):
        """
        Wrap perspective of the image based on rectangle coordinates.

        Args:
            img (numpy.ndarray): The image array.
            rect (numpy.ndarray): The rectangle coordinates.

        Returns:
            numpy.ndarray: The wrapped perspective image.
        """
        (tl, tr, br, bl) = rect
        width_a = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
        width_b = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
        height_a = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
        height_b = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
        max_width = max(int(width_a), int(width_b))
        max_height = max(int(height_a), int(height_b))
        dst = np.array([[0, 0], [max_width - 1, 0], [max_width - 1, max_height - 1],
                        [0, max_height - 1]], dtype="float32")
        m = cv2.getPerspectiveTransform(rect, dst)
        return cv2.warpPerspective(img, m, (max_width, max_height))

    def process_image(self):
        """
        Process the input image.

        This method performs various image processing steps 
        to prepare the image for text extraction.

        Returns:
            str: The extracted text from the processed image.
        """
        try:
            img = Image.open(self.file_name)
            img.thumbnail((600, 600), Image.LANCZOS)
            image = cv2.imread(self.file_name)
            resize_ratio = 500 / image.shape[0]
            original = image.copy()
            image = self.opencv_resize(image, resize_ratio)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            self.plot_gray(gray)
            blurred = cv2.GaussianBlur(gray, (5, 5), 0)
            self.plot_gray(blurred)
            rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))
            dilated = cv2.dilate(blurred, rect_kernel)
            self.plot_gray(dilated)
            edged = cv2.Canny(dilated, 100, 200, apertureSize=3)
            self.plot_gray(edged)
            contours, hierarchy = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            image_with_contours = cv2.drawContours(image.copy(), contours, -1, (0, 255, 0), 3)
            self.plot_rgb(image_with_contours)
            largest_contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
            image_with_largest_contours = cv2.drawContours(image.copy(), largest_contours, -1, (0, 255, 0), 3)
            self.plot_rgb(image_with_largest_contours)
            receipt_contour = self.get_receipt_contour(largest_contours)
            image_with_receipt_contour = cv2.drawContours(image.copy(), [receipt_contour], -1, (0, 255, 0), 2)
            self.plot_rgb(image_with_receipt_contour)
            scanned = self.wrap_perspective(original.copy(), self.contour_to_rect(receipt_contour, resize_ratio))
            plt.figure(figsize=(16, 10))
            plt.imshow(scanned)
            self.plot_gray(scanned)
            result_image_path = "./src/images/result.png"
            output = Image.fromarray(scanned)
            output.save(result_image_path)
            img = Image.open(result_image_path)
            text = pytesseract.image_to_string(img, lang="Armenian+eng")
            return text
        except cv2.error as e:
            print('Erooooooooooooooooooooooor', e)
            return ''