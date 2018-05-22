import numpy as np
from averageValue import averageValue


def nCC(imageA, imageB):
    heightA, widthA = imageA.shape
    heightB, widthB = imageB.shape
    averageA = averageValue(imageA)
    averageB = averageValue(imageB)

    wF = np.sum((imageA - averageA) * (imageB - averageB))
    W = np.sum((imageB - averageB)**2)
    F = np.sum((imageA - averageA)**2)
    gamma = (wF) / ((W * F)**(1/2))
    return gamma
