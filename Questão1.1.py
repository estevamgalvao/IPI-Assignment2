import numpy as np
import cv2
import glob

from rgb2YCbCr import RGB_YCbCr
from tookRGBPix import tookRBGPix

adress = "/home/estevamgalvao/Documentos/UnB/5º Semestre/Introdução ao Processamento de Imagens/ImageProcessing/Assignments/Assignment 2/Images/*.bmp"

imageArray = [cv2.imread(file) for file in glob.glob(adress)]
numImg = len(imageArray)

for img in imageArray:
    RGB_YCbCr(img, 1)

denoisedImage = np.zeros_like(imageArray[0], dtype = np.uint16)
for img in imageArray:
    denoisedImage += img
denoisedImage = denoisedImage / numImg
denoisedImage = denoisedImage.astype(np.int16)

cv2.imwrite("marcao.bmp", denoisedImage)

height, width, channels = denoisedImage.shape
borderedImage = np.full((height+4,width+4,3), 255)
borderedImage[2:height+2, 2:width+2] = denoisedImage[:, :]

cv2.imwrite("marcaoComBorda.bmp", borderedImage)
for i in range(2, width):
    for j in range(2, height):
        medianFilterList = tookRBGPix(borderedImage, i, j, 1)
        medianFilterList.sort()
        borderedImage[i, j, 1] = medianFilterList[4]

cv2.imwrite("marcaoMedianaSemBorda.bmp", borderedImage[2:width, 2:height, :])
RGB_YCbCr(borderedImage, 2)
cv2.imwrite("marcaoRGBMedian.bmp", borderedImage[2:width, 2:height, :])

# print(denoisedImage[6,6,0])
# print(borderedImage[8,8,0])