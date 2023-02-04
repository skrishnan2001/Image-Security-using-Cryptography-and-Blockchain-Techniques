''' Module to shuffle and reshuffle the pixels with chaos '''

import numpy as np


def shuffling(img, index, height, width):
    #height, width are the dimensions of the image
    shuffledImage = np.zeros(shape = [height, width, 3], dtype=np.uint8)
    for i in range(height):
        k = 0
        for j in range(width):
            shuffledImage[i][j] = img[i][index[k]]
            k += 1
    return shuffledImage


def reshuffling(img, index, height, width):
    #x, y are the dimensions of the image
    reshuffledImage = np.zeros(shape=[height, width, 3], dtype = np.uint8)

    for i in range(height):
        k = 0
        for j in range(width):
            reshuffledImage[i][index[k]] = img[i][j]
            k += 1
    return reshuffledImage
