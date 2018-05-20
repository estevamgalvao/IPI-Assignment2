import numpy as np

def notchPair(img, numPairs, dZero, uK, vK):
    height, width = img.shape
    # Crio duas matrizes para o Notch H e H- #
    hPlus  = np.ones((height, width), dtype=np.float16)
    hMinus = np.ones((height, width), dtype=np.float16)
    # Defino o centro #
    center = (height/2, width/2)
    # Para cada pixel aplico a enquação de Notch ButterWorth #
    for i in range(height):
        for j in range(width):
            dPlus  = ( ((i - center[0] - uK)**2) + ((j - center[1] - vK)**2) )**(1/2)
            dMinus = ( ((i - center[0] + uK)**2) + ((j - center[1] + vK)**2) )**(1/2)

            hPlus[i, j]   = (1/(1 + (dZero/dPlus)**(2*numPairs) ))
            hMinus[i, j]  = (1/(1 + (dZero/dMinus)**(2*numPairs) ))

    return hMinus * hPlus

def passNotchFilter(img, numPairs):
    # Função para chamar meus pares
    hFinal = notchPair(img, numPairs, 15, 73.29, 73.528)
    hFinal = hFinal * notchPair(img, numPairs, 15, -73.29, 73.528)
    hFinal = hFinal * notchPair(img, numPairs, 5, 218.844, 73.528)
    hFinal = hFinal * notchPair(img, numPairs, 5, -218.844, 73.528)
    hFinal = hFinal * notchPair(img, numPairs, 5, 72.719, 219.47)
    hFinal = hFinal * notchPair(img, numPairs, 5, -72.719, 219.47)

    return hFinal
