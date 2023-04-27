import cv2
from scipy import ndimage
import skimage
from skimage.morphology import disk
from skimage import filters
import numpy as np
from matplotlib import pyplot as plt
import PIL
from PIL import Image, ImageFilter, ImageOps


import scipy
class FiltreImage:
    def __init__(self,fichier1,fichier2 ):
        self.fichier1 = fichier1
        self.fichier2 = fichier2
        neighborhood = disk(radius=3)
        originale = Image.open(self.fichier1)
        originale = ImageOps.grayscale(originale)
        image = Image.open(self.fichier2)
        image2 = np.array(image)
        x = 10
        y = 10
        mean = cv2.blur(image2, (x, y))
        filtered = filters.rank.median(image2, neighborhood)
        median = Image.fromarray(filtered)
        affichage_comparaison(originale, image, mean, median)

        '''
        plt.subplot(2,3,4), plt.imshow(filtered3, cmap='gray')
        plt.title('Filtered Image (3 times)'), plt.xticks([]), plt.yticks([])
        plt.subplot(2, 3, 5), plt.imshow(filtered4, cmap='gray')
        plt.title('Filtered Image (n=5)'), plt.xticks([]), plt.yticks([])'''
        plt.show(block=True)




def affichage_comparaison(originale, bruitée, filtrée1, filtrée2):

    plt.subplot(2, 3, 1), plt.imshow(originale, cmap='gray')
    plt.title('Image originale'), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 3, 2), plt.imshow(bruitée, cmap='gray')
    plt.title('Image bruitée'), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 3, 3), plt.imshow(filtrée1, cmap='gray')
    plt.title('Mean filter'), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 3, 4), plt.imshow(filtrée2, cmap='gray')
    plt.title('Median filter'), plt.xticks([]), plt.yticks([])




'''noise = np.zeros(gray.shape, np.uint8)
cv2.randu(noise, 0, 255)
salt = noise > 245
pepper = noise < 10
gray[salt] = 255
gray[pepper] = 0'''
def main():
    image = FiltreImage("Images/stonk.png","Images/Stonk_G.png")

main()
