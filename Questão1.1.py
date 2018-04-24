import numpy as np
import cv2
import glob

from rgb2YCbCr import rgb2YCbCr

adress = "/home/estevamgalvao/Documentos/UnB/5º Semestre/Introdução ao Processamento de Imagens/ImageProcessing/Assignments/Assignment 2/Images/*.bmp"

imageArray = [cv2.imread(file) for file in glob.glob(adress)]
numImg = len(imageArray)

for img in imageArray:
    rgb2YCbCr(img)

denoisedImage = np.zeros_like(imageArray[0], dtype = np.uint16)

for img in imageArray:
    denoisedImage += img

denoisedImage = denoisedImage / numImg
denoisedImage = denoisedImage.astype(np.int16)



cv2.imwrite("marcao.bmp", denoisedImage)


