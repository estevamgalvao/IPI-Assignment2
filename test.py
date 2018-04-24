from rgb2YCbCr import rgb2YCbCr
import cv2


teste = cv2.imread("./Mars.bmp")

# print(teste[:,0])

rgb2YCbCr(teste)

cv2.imwrite("miranhagray.bmp", teste)