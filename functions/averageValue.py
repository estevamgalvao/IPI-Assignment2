import numpy as np

def averageValue(image):
    height, width = image.shape

    sum = float(np.sum(image))
    average = sum / (height * width)
    return average
