import numpy as np
import cv2
import glob

import notch_filter
from rgb_ycbcr import RGB_YCbCr
from tookRGBPix import tookRBGPix

adress = "/home/estevamgalvao/Documentos/UnB/5º Semestre/Introdução ao Processamento de Imagens/ImageProcessing/Assignments/Assignment 2/Images/*.bmp"
# Leio as imagens da pasta e salvo em uma lista. Logo após recupero o número de imagens lidas #
imageArray = [cv2.imread(file) for file in glob.glob(adress)]
numImg = len(imageArray)

# Recupero as medidas da primeira imagem
height, width, channels = imageArray[0].shape
# Crio um molde de zeros para acumular os pixels das imagens. uint16 -> garanto que não haverá overflow #
averageImage = np.zeros(height, width, dtype = np.uint16)

# Transformo cada imagem em YCbCr e acumulo os valores de seus pixels #
for img in imageArray:
    RGB_YCbCr(img, 1)
    averageImage += img[:, :, 0]

# Divido pelo número de imagens para os valores voltarem a ficar entre 0 - 255 #
averageImage /= numImg
# [x] AverageFilter #
cv2.imwrite("Average Image[Y].bmp", averageImage)
auxImage = np.zeros(height, width, channels, dtype = np.uint16)
auxImage[:, :, 0] = averageImage
auxImage[:, :, 1] = imageArray[0][:, :, 1]
auxImage[:, :, 2] = imageArray[0][:, :, 2]
cv2.imwrite("AuxImage-1.bmp", auxImage)



# Crio um molde com bordas para evitar out of range com uma máscara 3x3 andando pela imagem #
borderedImage = np.full((height+4,width+4,channels), 255, dtype = np.uint8)
# Colo o conteúdo da minha imagem no centro do molde #
borderedImage[2:height+2, 2:width+2] = auxImage[:, :]

# Passo o filtro pegando todos o pixels envolta do meu e selecionado o valor do meio "[4]" #
for i in range(2, width):
    for j in range(2, height):
        medianFilterList = tookRBGPix(borderedImage, i, j, 2)
        medianFilterList.sort()
        borderedImage[i, j, 1] = medianFilterList[4]

# Retiro as bordas #
medianImage = borderedImage[2:width, 2:height, :]
# [x] MedianFilter #
cv2.imwrite("Median Image.bmp", medianImage)


# Ultilizo a transformada de Fourier na componente Cb da Imagem Atual #
fourierImage = np.fft.fft2(medianImage[:, :, 1])
fourierImageShift = np.fft.fftshift(fourierImage)

magnitude_spectrum = 20 * np.log(np.abs(fourierImageShift))
cv2.imwrite("Magnitude Spectrum.bmp", magnitude_spectrum)

hFinal = notch_filter.passNotchFilter(fourierImageShift, 3)
tempImage = fourierImageShift * hFinal

unshiftedTempImage = np.fft.ifftshift(tempImage)
backImage = np.fft.ifft2(unshiftedTempImage)
backImage = np.int8(np.abs(backImage))

finalImage = medianImage
finalImage[:, :, 1] = backImage

RGB_YCbCr(finalImage, 2)

cv2.imwrite("FinalImage.bmp", finalImage)




























#
# print(hFinal.shape)
# print(fourierImageShift.shape)
#
# backImage = np.fft.ifftshift(tempImage[:, :])
# backImage = np.fft.ifft2(backImage)
# backImage = np.uint8(np.abs(backImage))
#
# print(tempImage.shape) #Ver melhor as dimensões da imagem, olhar na função se estou criando outras matrizes
# print(backImage.shape)
# print(medianImage[1].shape)
# cv2.imwrite("BackImage.bmp", backImage)
# medianImage[1] = backImage
#
#
#
#
# # # finalImage = cv2.merge([medianImage[0], finalImage, medianImage[2]])
# RGB_YCbCr(medianImage, 2)
# #
# cv2.imwrite("Final Image.bmp", medianImage)