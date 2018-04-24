import numpy as np

def rgb2YCbCr(img):
    height, width, channels = img.shape

    imageY = np.zeros((width, height, 1), dtype=np.uint16)
    imageCb = np.zeros((width, height, 1), dtype=np.uint16)
    imageCr = np.zeros((width, height, 1), dtype=np.uint16)

    imageY = (0.114 * img[:, :, 0] + 0.587 * img[:, :, 1] + 0.299 * img[:, :, 2])
    imageCb = 0.564 * (img[:, :, 0] - imageY)
    imageCr = 0.713 * (img[:, :, 2] - imageY)

    img[:, :, 0] = imageY
    img[:, :, 1] = imageCb
    img[:, :, 2] = imageCr

