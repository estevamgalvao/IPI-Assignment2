import numpy as np
import cv2

from rgb_ycbcr import RGB_YCbCr

mars = cv2.imread("Mars.bmp")

RGB_YCbCr(mars, 1)
cv2.imwrite("Meu YCRCB.bmp", mars)

RGB_YCbCr(mars, 2)
cv2.imwrite("Meu RGB.bmp", mars)