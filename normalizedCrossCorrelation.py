import numpy as np
import cv2

def nCC(imageA, imageB):
    heightA, widthA = imageA.shape
    heightB, widthB = imageB.shape
    sumW = float(np.sum(imageB))
    print(sumW)
    averageW = sumW / (heightB * widthB)
    if (averageW - int(averageW) > 0.5):
        averageW = int(averageW) + 1
    else:
        averageW = int(averageW)
    print(averageW)
    w = np.sum(imageB.astype("float") - averageW)
    # print(w)
    if w == 0:
        w = 1.0


    for y in range(heightA - heightB):
        for x in range(widthA - widthB):
            mask = imageA[y:y + heightB, x:x + widthB]
            sumF = float(np.sum(mask))
            averageF = sumF / (heightB * widthB)
            if (averageF - int(averageF) > 0.5):
                averageF = int(averageF) + 1
            else:
                averageF = int(averageF)

            f = np.sum(mask.astype("float") - averageF)
            # print(f)
            if f == 0:
                f = 1.0

            gamma = (w * f)/ ((w**2) * (f**2))**(1/2)
            # if gamma == 1:
            #     print("Achei um avião!")
    print(gamma)
