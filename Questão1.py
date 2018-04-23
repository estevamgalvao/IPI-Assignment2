import cv2
import datetime
import numpy
endereco = "/home/estevamgalvao/Documentos/UnB/5º Semestre/Introdução ao Processamento de Imagens/ImageProcessing/Assignments/Assignment 2/Images/1.bmp"

img = cv2.imread(endereco)
medianList = []


imgYCC = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
width, height, channels = img.shape
print(width, height, channels)

#consideramos um ruído, uma variável randomica que possui média zero.
#p = p0 + n => p0 é o pixel original e n é o ruído, logo se fizemos a média de N imagens desse pixel
#vamos obter p = p0 + n => p = p0
#usarei um filtro de mediana
#720/3 = 240 não irei usar padding
for j in range(height):
    for i in range(width):
        medianList.append(img[])



#componentes Y Cr Cb corrompidos pelo Gauss Noise. aplicar uma convolução para resolver isso antes de tudo.
cv2.imshow(endereco, img)
cv2.waitKey(0)

cv2.imshow(endereco, imgYCC)
cv2.waitKey(0)