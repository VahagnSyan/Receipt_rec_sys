'''
Module for picture preprocessing
'''


from PIL import Image
import pytesseract
import numpy as np
import cv2
import matplotlib.pyplot as plt


class Preprocessing:
    def __init__(self, file_name):
        self.file_name = file_name

    @staticmethod
    def opencv_resize(image, ratio):
        width = int(image.shape[1] * ratio)
        height = int(image.shape[0] * ratio)
        dim = (width, height)
        return cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

    @staticmethod
    def plot_rgb(image):
        plt.figure(figsize=(16, 10))
        return plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    @staticmethod
    def plot_gray(image):
        plt.figure(figsize=(16, 10))
        return plt.imshow(image, cmap="Greys_r")

    @staticmethod
    def approximate_contour(contour):
        peri = cv2.arcLength(contour, True)
        return cv2.approxPolyDP(contour, 0.032 * peri, True)

    @staticmethod
    def get_receipt_contour(contours):
        for c in contours:
            approx = Preprocessing.approximate_contour(c)
            if len(approx) == 4:
                return approx

    @staticmethod
    def contour_to_rect(contour, resize_ratio):
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
        (tl, tr, br, bl) = rect
        widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
        widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
        heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
        heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
        maxWidth = max(int(widthA), int(widthB))
        maxHeight = max(int(heightA), int(heightB))
        dst = np.array([[0, 0], [maxWidth - 1, 0], [maxWidth - 1, maxHeight - 1], [0, maxHeight - 1]], dtype="float32")
        M = cv2.getPerspectiveTransform(rect, dst)
        return cv2.warpPerspective(img, M, (maxWidth, maxHeight))

    def process_image(self):
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

        rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))
        dilated = cv2.dilate(blurred, rectKernel)
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

        RESULT_IMAGE_PATH = "./src/images/result.png"
        output = Image.fromarray(scanned)
        output.save(RESULT_IMAGE_PATH)

        img = Image.open(RESULT_IMAGE_PATH)

        text = pytesseract.image_to_string(img, lang="hye+eng")

        return text
