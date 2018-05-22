import numpy as np
import cv2
import copy

from functions.meanSquaredError import mse
from functions.rgb_ycbcr import RGB_YCbCr
from functions.normalizedCrossCorrelation import nCC

def planeFinder():
    print("Procurando...")

    DenoisedImage = cv2.imread("./aux_images/FinalImage.bmp")
    DenoisedImageYCbCr = copy.copy(DenoisedImage)
    RGB_YCbCr(DenoisedImageYCbCr, 1)
    height, width, channels = DenoisedImageYCbCr.shape

    croppedAirplane = DenoisedImageYCbCr[488:613, 408:495, 0]
    heightCrop, widthCrop = croppedAirplane.shape

    for y in range(height - heightCrop):
        for x in range(width - widthCrop):
            # nCC(DenoisedImageYCbCr[y:y+heightCrop, x:x+widthCrop, 0], croppedAirplane) # Está funcionando
            if mse(DenoisedImageYCbCr[y:y+heightCrop, x:x+widthCrop, 0], croppedAirplane) == 0:
                print("Achei um avião!")
                print("\t Está aqui: [%d, %d][%d, %d]" %(y, y+heightCrop, x, x+widthCrop))
                cv2.imshow('aviao encontrado', DenoisedImage[y:y+heightCrop, x:x+widthCrop])
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                print("Procurando...")
