import numpy as np
import cv2

from rgb_ycbcr import RGB_YCbCr

mars = cv2.imread("Mars.bmp")

RGB_YCbCr(mars, 1)
cv2.imwrite("Meu YCRCB.bmp", mars)

cv2.imwrite("Mars[0].bmp", mars[0])
cv2.imwrite("Mars[1].bmp", mars[1])
cv2.imwrite("Mars[2].bmp", mars[2])


RGB_YCbCr(mars, 2)
cv2.imwrite("Meu RGB.bmp", mars)