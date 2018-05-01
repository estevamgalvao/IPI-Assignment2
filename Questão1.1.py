import numpy as np
import cv2
import glob

from rgb_ycbcr import RGB_YCbCr
from tookRGBPix import tookRBGPix

adress = "/home/estevamgalvao/Documentos/UnB/5º Semestre/Introdução ao Processamento de Imagens/ImageProcessing/Assignments/Assignment 2/Images/*.bmp"

imageArray = [cv2.imread(file) for file in glob.glob(adress)]
numImg = len(imageArray)

for img in imageArray:
    RGB_YCbCr(img, 1)

print("Image Array: ", imageArray[0].dtype)

averageImage = np.zeros_like(imageArray[0], dtype = np.uint16)
print("Average Image: ", averageImage.dtype)
for img in imageArray:
    averageImage += img
averageImage = averageImage / numImg
averageImage = averageImage.astype(np.int16)

print("Average Image - Pós: ", averageImage.dtype)
cv2.imwrite("marcao.bmp", averageImage)

height, width, channels = averageImage.shape
borderedImage = np.full((height+4,width+4,3), 255, dtype = np.uint8)
borderedImage[2:height+2, 2:width+2] = averageImage[:, :]

print("Bordered Image: ", borderedImage.dtype)

#cv2.imwrite("marcaoComBorda.bmp", borderedImage)
for i in range(2, width):
    for j in range(2, height):
        medianFilterList = tookRBGPix(borderedImage, i, j, 1)
        medianFilterList.sort()
        borderedImage[i, j, 1] = medianFilterList[4]

medianImage = borderedImage[2:width, 2:height, :]
print("Median Image: ", medianImage.dtype)

#cv2.imwrite("marcaoMedianaSemBorda.bmp", medianImage)
cv2.imwrite("Median Image.bmp", medianImage)
RGB_YCbCr(medianImage, 2)
# medianImage = cv2.cvtColor(medianImage, cv2.COLOR_YCR_CB2BGR)
cv2.imwrite("Median Image RGB.bmp", medianImage)
#imgRBG2 = cv2.cvtColor(teste, cv2.COLOR_YCR_CB2BGR)

# print(averageImage[6,6,0])
# print(borderedImage[8,8,0])