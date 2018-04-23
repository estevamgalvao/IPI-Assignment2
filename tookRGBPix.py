def tookRBGPix(img, i, j, option):
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
        print("não fode")