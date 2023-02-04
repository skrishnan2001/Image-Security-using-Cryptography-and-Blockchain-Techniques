'''
Image Encryption: Substitution + Transposition
'''

import keygen as kg
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def indexgen(x, r, n): #Optimized -> O(n log n)
    index = []
    k = []

    for i in range(n):
        x = r * x * (1 - x) # Logistic Map
        k.append(x) # Generating the key
        index.append(i) # Generating the index

    zipped = zip(k, index) # Zip the two lists together
    sorted_zipped = sorted(zipped) # Sort the zipped list
    sorted_k, sorted_index = zip(*sorted_zipped) # Unzip the sorted list back into separate lists

    return sorted_index

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
    encryptedImage = encrypt(img, key, height, width)
    plt.imshow(encryptedImage)
    plt.show()
    plt.imsave('Images/'+ImageName+'_EncryptedImage'+ext, encryptedImage)

    #Step 4: Shuffling the pixels in the encrypted image
    shuffleKey = indexgen(0.1, 3.91, width)
    shuffledImage = shuffling(encryptedImage, shuffleKey, height, width)
    plt.imshow(shuffledImage)
    plt.show()

    #Step 5: Re-Shuffling the pixels to get the encrypted image before shuffling
    shuffleKey = indexgen(0.1, 3.91, width)
    reshuffledImage = reshuffling(shuffledImage, shuffleKey, height, width)
    plt.imshow(reshuffledImage)
    plt.show()

    #Step 6: Decrypting the encrypted image to retrieve the original image
    decyptedImage = decrypt(reshuffledImage, key, height, width)
    plt.imshow(decyptedImage)
    plt.show()
    plt.imsave('Images/'+ImageName+'_DecryptedImage'+ext, decyptedImage)
