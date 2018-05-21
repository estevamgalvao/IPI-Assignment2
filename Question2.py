import numpy as np
import cv2
from functions.rgb_ycbcr import RGB_YCbCr

print("Procurando...\n"*15)

def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    # return the MSE, the lower the error, the more "similar"
    # the two images are
    return err

# croppedAirplane = cv2.imread("cropped_plane.bmp")
# height, width, channels = croppedAirplane.shape
# RGB_YCbCr(croppedAirplane, 1)


########################################################
DenoisedImage = cv2.imread("./aux_images/FinalImage.bmp")
RGB_YCbCr(DenoisedImage, 1)
height, width, channels = DenoisedImage.shape

croppedAirplane = DenoisedImage[488:613, 408:495, 0]
heightCut, widthCut = croppedAirplane.shape
cv2.imshow('cropped', croppedAirplane)
cv2.waitKey(0)
cv2.destroyAllWindows()

for y in range(height - heightCut):
    for x in range(width - widthCut):
        if mse(DenoisedImage[y:y+heightCut, x:x+widthCut, 0], croppedAirplane) == 0:
            print("Achei um avião!")
            print("\t Intervalo de Coordenadas: [%d, %d][%d, %d]" %(y, y+heightCut, x, x+widthCut))

# sum = float(np.sum(croppedAirplane[:, :, 0]))
# print(sum)
#
# averageW = sum/(len(croppedAirplane) * len(croppedAirplane[0]))
# if (averageW - int(averageW) > 0.5):
#     averageW = int(averageW) + 1
# else:
#     averageW = int(averageW)
# print(averageW)

# Eu acredito q o resultado seja no canto superior esquerdo da template
# X e y são o local por onde a qual ocorre a operação, e s e t são  as dimensões da template