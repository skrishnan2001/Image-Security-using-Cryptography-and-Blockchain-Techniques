'''
Image Encryption and Decryption by XOR Substitution Approach
'''
import numpy as np

#Encryption-Substitution with XOR
def encrypt(img, key, height, width):
    z = 0
    encryptedImage = np.zeros(shape=[height, width, 3], dtype=np.uint8)
    for i in range(height):
        for j in range(width):
            #pixel value XORed with key
            encryptedImage[i, j] = img[i, j] ^ key[z]
            z += 1
    return encryptedImage


#Decryption
def decrypt(reshuffledImage, key, height, width):
    z=0
    decyptedImage = np.zeros(shape = [height, width, 3], dtype = np.uint8)
    for i in range(height):
        for j in range(width):
            decyptedImage[i, j] = reshuffledImage[i, j] ^ key[z]
            z += 1
    return decyptedImage
