def rgb2grey(height, width, img): # Faço a conversão e atribuo o mesmo valor a todos os 3 planos, deixando-a em escala de cinza, porém ainda RGB
    for i in range(height):
        for j in range(width):
            img[i, j] = (0.114 * img[i, j, 0] + #pixel da matriz azul
                         0.587 * img[i, j, 1] + #pixel da matriz verde
                         0.299 * img[i, j, 2])  #pixel da matriz vermelha
    return img