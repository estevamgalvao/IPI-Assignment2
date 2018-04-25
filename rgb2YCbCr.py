import numpy as np

def RGB_YCbCr(img, option):
    height, width, channels = img.shape

    if (option == 1):
        imageY = np.zeros((width, height, 1), dtype=np.uint8)
        imageCb = np.zeros((width, height, 1), dtype=np.uint8)
        imageCr = np.zeros((width, height, 1), dtype=np.uint8)

        imageY = (0.114 * img[:, :, 0] + 0.587 * img[:, :, 1] + 0.299 * img[:, :, 2])
        imageCb = 0.564 * (img[:, :, 0] - imageY)
        imageCr = 0.713 * (img[:, :, 2] - imageY)

        img[:, :, 0] = imageY
        img[:, :, 1] = imageCb
        img[:, :, 2] = imageCr

    elif (option == 2):
        imageR = np.zeros((width, height, 1), dtype=np.uint8)
        imageG = np.zeros((width, height, 1), dtype=np.uint8)
        imageB = np.zeros((width, height, 1), dtype=np.uint8)

        imageR = img[:, :, 0] + (1.402 * img[:, :, 2])
        imageG = img[:, :, 0] - (0.344 * img[:, :, 1]) - (0.714 * img[:, :, 2])
        imageB = img[:, :, 0] + (1.772 * img[:, :, 1])

        img[:, :, 0] = imageB
        img[:, :, 1] = imageG
        img[:, :, 2] = imageR

    else:
        print("não fode, moai")