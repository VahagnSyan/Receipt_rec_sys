import cv2
import imutils
import matplotlib.pyplot as plt
from PIL import Image

def orient_vertical(img):
    width = img.shape[1]
    height = img.shape[0]
  
    if width > height:
      rotated = imutils.rotate(img, angle=270)
    else:
      rotated = img
    return rotated

raw_path = '1.png' # Enter the path to your scanned receipt
raw_img = cv2.imread(raw_path)

# View the image in RGB
raw_rgb = cv2.cvtColor(orient_vertical(raw_img), cv2.COLOR_BGR2RGB)
plt.imshow(raw_rgb)
plt.show()
