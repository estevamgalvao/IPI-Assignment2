import sys
import math
import numpy as np
import cv2
import matplotlib.pyplot as plt
import glob
import os
from rgb_ycbcr import RGB_YCbCr

img = cv2.imread('Median Image.bmp') # Me retorna apenas 1 canal, não sei como ele decide os valores
img2 = cv2.imread('Mars.bmp')


def Frequency_domain_filtering(img):
    # FFT and spectrum process
    Fourier_img = np.fft.fft2(img)
    Fourier_img_shift = np.fft.fftshift(Fourier_img)
    magnitude_spectrum = 20 * np.log(np.abs(Fourier_img_shift))

    plt.subplot(121), plt.imshow(img, cmap='gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    plt.savefig('Magnitude_spectrum_before')

    height = img.shape[0]
    width = img.shape[1]
    H = np.zeros((height, width), np.int16)
    Hp = np.zeros((height, width), np.int16)



    # Filtering
    Hp = Notch_filter(Fourier_img_shift, 218.844, 73.528, 5)
    H[:, :] = Hp[:, :]

    Hp = Notch_filter(Fourier_img_shift, 73.29, 73.528, 15)
    H[:, :] = H[:, :] * Hp[:, :]

    Hp = Notch_filter(Fourier_img_shift, -73.29, 73.528, 15)
    H[:, :] = H[:, :] * Hp[:, :]

    Hp = Notch_filter(Fourier_img_shift, -218.844, 73.528, 5)
    H[:, :] = H[:, :] * Hp[:, :]

    Hp = Notch_filter(Fourier_img_shift, 72.719, 219.47, 5)
    H[:, :] = H[:, :] * Hp[:, :]

    Hp = Notch_filter(Fourier_img_shift, -72.719, 219.47, 5)
    H[:, :] = H[:, :] * Hp[:, :]

    img_filt = Fourier_img_shift[:, :] * H[:, :]

    # Inverse Fourier's tranform
    Inverse_img_filt = np.fft.ifftshift(img_filt)
    img_back = np.fft.ifft2(Inverse_img_filt)
    img_back = np.abs(img_back)

    return img_back