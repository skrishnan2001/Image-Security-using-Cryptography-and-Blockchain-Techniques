'''
Driver Code for Image Encryption and Decryption using Substitution + Transposition
'''

import keygen as kg
import encryption_decryption as ed
import shuffling_reshuffling as sr
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


if __name__=='__main__':
    #Step 1: Loading / Reading the image
    ImageName = "Novak"
    ext = ".jpg"
    img = mpimg.imread('Images/'+ImageName+ext)
    plt.imshow(img)
    plt.show()

    #Step 2: Generating chaotic keys
    height = img.shape[0]
    width = img.shape[1]
    key = kg.keygen(0.01, 3.95, height * width)
    #print("Key = ", key)

    #Step 3: Encrypting the original image
    encryptedImage = ed.encrypt(img, key, height, width)
    plt.imshow(encryptedImage)
    plt.show()
    plt.imsave('Images/'+ImageName+'_EncryptedImage'+ext, encryptedImage)

    #Step 4: Shuffling the pixels in the encrypted image
    shuffleKey = kg.indexgen(0.1, 3.91, width)
    shuffledImage = sr.shuffling(encryptedImage, shuffleKey, height, width)
    plt.imshow(shuffledImage)
    plt.show()

    #Step 5: Re-Shuffling the pixels to get the encrypted image before shuffling
    shuffleKey = kg.indexgen(0.1, 3.91, width)
    reshuffledImage = sr.reshuffling(shuffledImage, shuffleKey, height, width)
    plt.imshow(reshuffledImage)
    plt.show()

    #Step 6: Decrypting the encrypted image to retrieve the original image
    decyptedImage = ed.decrypt(reshuffledImage, key, height, width)
    plt.imshow(decyptedImage)
    plt.show()
    plt.imsave('Images/'+ImageName+'_DecryptedImage'+ext, decyptedImage)
