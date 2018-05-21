import numpy as np
import cv2
from functions.rgb_ycbcr import RGB_YCbCr
from normalizedCrossCorrelation import nCC

print("Procurando...\n"*15)

def mse(imageA, imageB):
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    return err



########################################################
DenoisedImage = cv2.imread("./aux_images/FinalImage.bmp")
RGB_YCbCr(DenoisedImage, 1)
height, width, channels = DenoisedImage.shape

croppedAirplane = DenoisedImage[488:613, 408:495, 0]
heightCut, widthCut = croppedAirplane.shape
cv2.imshow('cropped', croppedAirplane)
cv2.waitKey(0)
cv2.destroyAllWindows()

nCC(DenoisedImage[:, :, 0], croppedAirplane)



# for y in range(height - heightCut):
#     for x in range(width - widthCut):
#         if mse(DenoisedImage[y:y+heightCut, x:x+widthCut, 0], croppedAirplane) == 0:
#             print("Achei um avião!")
#             print("\t Está aqui: [%d, %d][%d, %d]" %(y, y+heightCut, x, x+widthCut))
#

# Eu acredito q o resultado seja no canto superior esquerdo da template
# X e y são o local por onde a qual ocorre a operação, e s e t são  as dimensões da template