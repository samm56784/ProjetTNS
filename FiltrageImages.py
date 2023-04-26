import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Images/Stonk_SAP.png')
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
noise = np.zeros(gray.shape, np.uint8)
cv2.randu(noise, 0, 255)
salt = noise > 245
pepper = noise < 10
gray[salt] = 255
gray[pepper] = 0

filtered = cv2.medianBlur(img, 3)


plt.subplot(131),plt.imshow(img2, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(filtered, cmap='gray')
plt.title('Filtered Image'), plt.xticks([]), plt.yticks([])
plt.show()