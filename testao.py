import numpy as np
import cv2

from rgb_ycbcr import RGB_YCbCr

mars = cv2.imread("Mars.bmp")
teste = cv2.imread("marcaoMedianaSemBorda.bmp")
print("Teste: ", teste.dtype)

imgYCC = cv2.cvtColor(mars, cv2.COLOR_BGR2YCR_CB)

RGB_YCbCr(mars, 1)

cv2.imwrite("Mars_YCbCr.bmp", mars)
cv2.imwrite("Mars_YCbCrDOIS.bmp", imgYCC)

imgRBG = cv2.cvtColor(imgYCC, cv2.COLOR_YCR_CB2BGR)

imgRBG2 = cv2.cvtColor(teste, cv2.COLOR_YCR_CB2BGR)
print(imgRBG2.dtype)

cv2.imwrite("Mars_RGBDOIS.bmp", imgRBG)
cv2.imwrite("Teste.bmp", imgRBG2)


RGB_YCbCr(mars, 2)
cv2.imwrite("Mars_RGB.bmp", mars)
