import numpy as np
import cv2
import glob
import copy
from functions.notch_filter import passNotchFilter
from functions.rgb_ycbcr import RGB_YCbCr
from functions.tookRGBPix import tookRBGPix

def Denoise():
    adress = "/home/estevamgalvao/Documentos/UnB/5º Semestre/Introdução ao Processamento de Imagens/ImageProcessing/Assignments/Assignment 2/Images/*.bmp"
    # Leio as imagens da pasta e salvo em uma lista. Logo após recupero o número de imagens lidas #
    imageArray = [cv2.imread(file) for file in glob.glob(adress)]
    numImg = len(imageArray)

    # Recupero as medidas da primeira imagem
    height, width, channels = imageArray[0].shape

    # Crio um molde de zeros para acumular os pixels das imagens. uint16 -> garanto que não haverá overflow #
    averageImage = np.zeros((height, width), dtype = np.uint16)

    # Transformo cada imagem em YCbCr e acumulo os valores de seus pixels #
    for img in imageArray:
        RGB_YCbCr(img, 1)
        averageImage += img[:, :, 0]

    # Divido pelo número de imagens para os valores voltarem a ficar entre 0 - 255 #
    averageImage = averageImage / numImg
    # [x] AverageFilter #
    cv2.imwrite("Average Image[Y].bmp", averageImage)
    auxImage = imageArray[0]
    auxImage[:, :, 0] = averageImage
    cv2.imwrite("./aux_images/AuxImage-1.bmp", auxImage)
    auxImage2 = copy.copy(auxImage)
    RGB_YCbCr(auxImage2, 2)
    cv2.imwrite("./aux_images/AuxImage-1RGB.bmp", auxImage2)

    # Crio um molde com bordas para evitar out of range com uma máscara 3x3 andando pela imagem #
    borderedImage = np.full((height+2,width+2), 255, dtype = np.uint8)
    # Colo o conteúdo da minha imagem no centro do molde #
    borderedImage[1:-1, 1:-1] = auxImage[:, :, 2]

    # Passo o filtro pegando todos o pixels envolta do meu e selecionado o valor do meio "[4]" #
    for i in range(1, width):
        for j in range(1, height):
            medianFilterList = tookRBGPix(borderedImage, i, j)
            medianFilterList.sort()
            borderedImage[i, j] = medianFilterList[4]

    # Retiro as bordas #
    medianImage = borderedImage[1:-1, 1:-1]
    # [x] MedianFilter #
    cv2.imwrite("Median Image[CR].bmp", medianImage)
    auxImage[:, :, 2] = medianImage
    cv2.imwrite("./aux_images/AuxImage-2.bmp", auxImage)
    auxImage2 = copy.copy(auxImage)
    RGB_YCbCr(auxImage2, 2)
    cv2.imwrite("./aux_images/AuxImage-2RGB.bmp", auxImage2)

    # Utilizo a transformada de Fourier na componente Cb da Imagem Atual #
    fourierImage = np.fft.fft2(auxImage[:, :, 1])
    fourierImageShift = np.fft.fftshift(fourierImage)
    # Espectro de Magnitude da componente Cb #
    magnitude_spectrum = 20 * np.log(np.abs(fourierImageShift))
    cv2.imwrite("Magnitude Spectrum.bmp", magnitude_spectrum)
    # Realizo a filtragem Notch #
    hFinal = passNotchFilter(fourierImageShift, 3)
    tempImage = fourierImageShift * hFinal
    # Transformo a imagem de volta para o domínio do espaço #
    unshiftedTempImage = np.fft.ifftshift(tempImage)
    backImage = np.fft.ifft2(unshiftedTempImage)
    backImage = np.int8(np.abs(backImage))

    # [x] FourierFilter #
    cv2.imwrite("Back Image[CB].bmp", backImage)

    # Segunda passada do filtro da Mediana #
    borderedImage[1:-1, 1:-1] = backImage
    for i in range(1, height):
        for j in range(1, width):
            medianFilterList = tookRBGPix(borderedImage, i, j)
            medianFilterList.sort()
            borderedImage[i, j] = medianFilterList[4]
    auxImage[:, :, 1] = borderedImage[1:-1, 1:-1]


    # Converto para RGB novamente #
    RGB_YCbCr(auxImage, 2)
    cv2.imwrite("./aux_images/FinalImage.bmp", auxImage)
    print("Image was denoised")
