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
    def __init__(self,fichier1,fichier2,i,ii,iii ):
        self.i = i
        self.iii = iii
        self.fichier1 = fichier1
        self.fichier2 = fichier2
        neighborhood = disk(radius=iii)
        originale = Image.open(self.fichier1)
        originale = ImageOps.grayscale(originale)
        image = Image.open(self.fichier2)
        image2 = np.array(image)
        x = 10
        y = 10
        mean = cv2.blur(image2, (x, y))

        filtered = image2
        for x in range(ii):
            filtered = filters.rank.median(filtered, neighborhood)
            x = x + 1
        median = Image.fromarray(filtered)
        affichage_comparaison(originale, image, mean, median, self.i)
        mean2 = Image.fromarray(mean)
        enregistrement(median, self.fichier2, "median")
        enregistrement(mean2, self.fichier2, "mean")






def affichage_comparaison(originale, bruitée, filtrée1, filtrée2,i):

    plt.figure(i)
    plt.subplot(2, 3, 1), plt.imshow(originale, cmap='gray')
    plt.title('Image originale'), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 3, 2), plt.imshow(bruitée, cmap='gray')
    plt.title('Image bruitée'), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 3, 3), plt.imshow(filtrée1, cmap='gray')
    plt.title('Mean filter'), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 3, 4), plt.imshow(filtrée2, cmap='gray')
    plt.title('Median filter'), plt.xticks([]), plt.yticks([])
    plt.show(block=False)

def comparaison_deux_images(image1, image2, nom1, nom2,i):
    plt.figure(i)
    plt.subplot(2, 3, 1), plt.imshow(image1, cmap='gray')
    plt.title(nom1), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 3, 2), plt.imshow(image2, cmap='gray')
    plt.title(nom2), plt.xticks([]), plt.yticks([])

def enregistrement(image, fichier, type):
    if "G" in fichier:
        fichier = fichier.replace("Images/","Images/G/")
        fichier = fichier.replace(".png","")
        fichier = fichier + "_"+type+"_filtered.png"
        image.save(fichier)
    elif "SAP" in fichier:
        fichier = fichier.replace("Images/", "Images/SAP/")
        fichier = fichier.replace(".png", "")
        fichier = fichier + "_" + type + "_filtered.png"
        image.save(fichier)


def main():
    image1 = FiltreImage("Images/stonk.png","Images/Stonk_G.png",  1, 2, 2)
    image2 = FiltreImage("Images/stonk.png","Images/Stonk_SAP.png",2,1,3)
    image3 = FiltreImage("Images/LinkedIn_logo_initials.png","Images/LinkedIn_G.png", 3,5,3 )
    image4 = FiltreImage("Images/LinkedIn_logo_initials.png", "Images/LinkedIn_SAP.png",4,1,3)
    plt.show()
    im = Image.open("Images/LinkedIn_logo_initials.png")
    im2 = Image.open("Images/stonk.png")
    im = ImageOps.grayscale(im)
    im2= ImageOps.grayscale(im2)
    im.save("Images/LinkedIn_logo_initials_grayscale.png")
    im2.save("Images/stonk_grayscale.png")

main()
