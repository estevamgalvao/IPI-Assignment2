def tookRBGPix(img, i, j, option = 3):
    blue = []
    green = []
    red = []

    if option == 0:
        blue.append(img[i-1, j+1, 0])
        blue.append(img[i, j+1, 0])
        blue.append(img[i+1, j+1, 0])
        blue.append(img[i-1, j, 0])
        blue.append(img[i, j, 0])
        blue.append(img[i+1, j, 0])
        blue.append(img[i-1, j-1, 0])
        blue.append(img[i, j-1, 0])
        blue.append(img[i+1, j-1, 0])
        return blue

    elif option == 1:
        green.append(img[i - 1, j + 1, 1])
        green.append(img[i, j + 1, 1])
        green.append(img[i + 1, j + 1, 1])
        green.append(img[i - 1, j, 1])
        green.append(img[i, j, 1])
        green.append(img[i + 1, j, 1])
        green.append(img[i - 1, j - 1, 1])
        green.append(img[i, j - 1, 1])
        green.append(img[i + 1, j - 1, 1])
        return green

    elif option == 2:
        red.append(img[i - 1, j + 1, 2])
        red.append(img[i, j + 1, 2])
        red.append(img[i + 1, j + 1, 2])
        red.append(img[i - 1, j, 2])
        red.append(img[i, j, 2])
        red.append(img[i + 1, j, 2])
        red.append(img[i - 1, j - 1, 2])
        red.append(img[i, j - 1, 2])
        red.append(img[i + 1, j - 1, 2])
        return red
    else:
        blue.append(img[i - 1, j + 1])
        blue.append(img[i, j + 1])
        blue.append(img[i + 1, j + 1])
        blue.append(img[i - 1, j])
        blue.append(img[i, j])
        blue.append(img[i + 1, j])
        blue.append(img[i - 1, j - 1])
        blue.append(img[i, j - 1])
        blue.append(img[i + 1, j - 1])
        return blue