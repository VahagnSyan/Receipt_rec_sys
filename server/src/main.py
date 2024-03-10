from PIL import Image
import pytesseract
from db.connect_db import connect_db
import numpy as np
import cv2
import matplotlib.pyplot as plt

from skimage.filters import threshold_local
from PIL import Image


file_name = "./src/images/4.jpg"
img = Image.open(file_name)
img.thumbnail((600, 600), Image.LANCZOS)


def opencv_resize(image, ratio):
    width = int(image.shape[1] * ratio)
    height = int(image.shape[0] * ratio)
    dim = (width, height)
    return cv2.resize(image, dim, interpolation=cv2.INTER_AREA)


def plot_rgb(image):
    plt.figure(figsize=(16, 10))
    return plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))


def plot_gray(image):
    plt.figure(figsize=(16, 10))
    return plt.imshow(image, cmap="Greys_r")


image = cv2.imread(file_name)
resize_ratio = 500 / image.shape[0]
original = image.copy()
image = opencv_resize(image, resize_ratio)


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plot_gray(gray)


blurred = cv2.GaussianBlur(gray, (5, 5), 0)
plot_gray(blurred)


rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))
dilated = cv2.dilate(blurred, rectKernel)
plot_gray(dilated)

edged = cv2.Canny(dilated, 100, 200, apertureSize=3)
plot_gray(edged)


# Detect all contours in Canny-edged image
contours, hierarchy = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
image_with_contours = cv2.drawContours(image.copy(), contours, -1, (0, 255, 0), 3)
plot_rgb(image_with_contours)

# Get 10 largest contours
largest_contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
image_with_largest_contours = cv2.drawContours(image.copy(), largest_contours, -1, (0, 255, 0), 3)
plot_rgb(image_with_largest_contours)


def approximate_contour(contour):
    peri = cv2.arcLength(contour, True)
    return cv2.approxPolyDP(contour, 0.032 * peri, True)


def get_receipt_contour(contours):
    # loop over the contours
    for c in contours:
        approx = approximate_contour(c)
        # if our approximated contour has four points, we can assume it is receipt's rectangle
        if len(approx) == 4:
            return approx


get_receipt_contour(largest_contours)

receipt_contour = get_receipt_contour(largest_contours)
image_with_receipt_contour = cv2.drawContours(image.copy(), [receipt_contour], -1, (0, 255, 0), 2)
plot_rgb(image_with_receipt_contour)


def contour_to_rect(contour):
    pts = contour.reshape(4, 2)
    rect = np.zeros((4, 2), dtype="float32")
    # top-left point has the smallest sum
    # bottom-right has the largest sum
    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]
    # compute the difference between the points:
    # the top-right will have the minumum difference
    # the bottom-left will have the maximum difference
    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]
    return rect / resize_ratio


def wrap_perspective(img, rect):
    # unpack rectangle points: top left, top right, bottom right, bottom left
    (tl, tr, br, bl) = rect
    # compute the width of the new image
    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    # compute the height of the new image
    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    # take the maximum of the width and height values to reach
    # our final dimensions
    maxWidth = max(int(widthA), int(widthB))
    maxHeight = max(int(heightA), int(heightB))
    # destination points which will be used to map the screen to a "scanned" view
    dst = np.array([[0, 0], [maxWidth - 1, 0], [maxWidth - 1, maxHeight - 1], [0, maxHeight - 1]], dtype="float32")
    # calculate the perspective transform matrix
    M = cv2.getPerspectiveTransform(rect, dst)
    # warp the perspective to grab the screen
    return cv2.warpPerspective(img, M, (maxWidth, maxHeight))


def check_receipt_angle(text):
    return "Արարատ Սուպերմարկետ" in text.split("\n")


def rotate_image_90(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Rotate the image by 90 degrees counterclockwise
    rotated_image = cv2.transpose(image)
    rotated_image = cv2.flip(rotated_image, 0)

    # Save the rotated image, replacing the original file
    cv2.imwrite(image_path, rotated_image)


scanned = wrap_perspective(original.copy(), contour_to_rect(receipt_contour))
plt.figure(figsize=(16, 10))
plt.imshow(scanned)


plot_gray(scanned)

RESULT_IMAGE_PATH = "./src/images/result.png"
output = Image.fromarray(scanned)
output.save(RESULT_IMAGE_PATH)


img = Image.open(RESULT_IMAGE_PATH)

text = pytesseract.image_to_string(img, lang="hye+eng")

for i in range(3):
    if check_receipt_angle(text):
        #print(text)
        break
    rotate_image_90(RESULT_IMAGE_PATH)
    img = Image.open(RESULT_IMAGE_PATH)
    text = pytesseract.image_to_string(img, lang="hye+eng")


def filter(info) -> list:
    result = []
    index = 2
    while index < len(info):
        # if 'Դաս' in info[index] or 'Դամ' in info[index] or 'Դպա' in info[index]:
        #     result.append(info[index + 1] + '\t\t' + info[index + 2].split(' ')[-1])

        if (
            "Հատ" in info[index]
            or "Յ1ատ" in info[index]
            or "Յատ" in info[index]
            or "Վատ" in info[index]
            or "գի" in info[index]
            or "կգ" in info[index]
            or "գր" in info[index]
        ):
            result.append(info[index] + "\t\t" + info[index + 1].split(" ")[-1])

        if "Ընդամենը" in info[index]:
            result.append(info[index])
        index += 1
    return result


def show(info):
    text = info.split("\n")
    text2 = [x for x in text if x != ""]
    for i in filter(text2):
        print(i)
    print()


show(text)
print(text)

# connect_db()
