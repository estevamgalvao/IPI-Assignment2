import numpy as np
import cv2
from functions.rgb_ycbcr import RGB_YCbCr

croppedAirplane = cv2.imread("cropped_plane.bmp")
height, width, channels = croppedAirplane.shape

print(len(croppedAirplane))
print(len(croppedAirplane[0]))

RGB_YCbCr(croppedAirplane, 1)

pTable = {}
maior = 0
for i in range(height):
    for j in range(width):
        if croppedAirplane[i, j, 0] in pTable:
            pTable[croppedAirplane[i, j, 0]] += 1
            if pTable[croppedAirplane[i, j, 0]] > maior:
                maior = pTable[croppedAirplane[i, j, 0]]
                maiorAdress = croppedAirplane[i, j, 0]
        else:
            pTable[croppedAirplane[i, j, 0]] = 1

print(pTable)
print(maior)
print(maiorAdress)