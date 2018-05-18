import numpy as np
import cv2
import glob

from rgb_ycbcr import RGB_YCbCr
from tookRGBPix import tookRBGPix

adress = "/home/estevamgalvao/Documentos/UnB/5º Semestre/Introdução ao Processamento de Imagens/ImageProcessing/Assignments/Assignment 2/Images/*.bmp"

imageArray = [cv2.imread(file) for file in glob.glob(adress)] # Leio todas as imagens da pasta localizada em "adress" e salvo em uma lista
numImg = len(imageArray) # Conto quantas imagens foram lidas


for img in imageArray: # Cada imagem é transformada em YCbCr
    RGB_YCbCr(img, 1)

# print("Image Array: ", imageArray[0].dtype)

averageImage = np.zeros_like(imageArray[0], dtype = np.uint16) # Crio uma matriz cheia de zeros do tamanho da primeira imagem para servir de forma para ImagemMédia
# uint16 porque assim garanto que a soma dos pixels de cada imagem não irá dar overflow
# print("Average Image: ", averageImage.dtype)

for img in imageArray: # Vou acumulando os valores dos pixels no meu molde
    averageImage += img

averageImage = averageImage / numImg # Divido pelo número de imagens para os valores voltarem a ficar entre 0 - 255
# averageImage = averageImage.astype(np.int16)

# print("Average Image - Pós: ", averageImage.dtype)
cv2.imwrite("marcao.bmp", averageImage) # Salvo a ImagemMédia, filtrada pelo filtro da Média

height, width, channels = averageImage.shape # Recupero as medidas do meu molde para criar uma imagem bordada e passar meu filtro Mediana por ela
borderedImage = np.full((height+4,width+4,3), 255, dtype = np.uint8)
borderedImage[2:height+2, 2:width+2] = averageImage[:, :]

# print("Bordered Image: ", borderedImage.dtype)

for i in range(2, width): # Passo o filtro pegando todos o pixels envolta do meu e selecionado o valor do meio "[4]"
    for j in range(2, height):
        medianFilterList = tookRBGPix(borderedImage, i, j, 1)
        medianFilterList.sort()
        borderedImage[i, j, 1] = medianFilterList[4]

medianImage = borderedImage[2:width, 2:height, :] # Retiro as bordas
# print("Median Image: ", medianImage.dtype)

cv2.imwrite("Median Image.bmp", medianImage) # Salvo minha imagem filtrada pela Mediana
RGB_YCbCr(medianImage, 2) # Volto ela para RGB
cv2.imwrite("Median Image RGB.bmp", medianImage) # Salvo a imagem colorida

medianImageGrey = cv2.imread("Median Image RGB.bmp", 0)

Fourier_img = np.fft.fft2(medianImageGrey)
Fourier_img_shift = np.fft.fftshift(Fourier_img)
magnitude_spectrum = 20 * np.log(np.abs(Fourier_img_shift))

cv2.imwrite("Magnitude Spectrum.bmp", magnitude_spectrum)



