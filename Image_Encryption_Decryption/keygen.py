"""
Function to generate key using a chaotic map for an image encryption / decryption process (substitution)
x: Initial Condition
r: Control Parameter
size: Number of keys to be generated
"""
def keygen(x, r, size):
    key = []
    for i in range(size):
        x = r * x * (1 - x) #Logistic Map
        key.append(int((x * pow(10, 16)) % 256))
    return key


"""
Function to transposition key index list using a logistic chaotic map for an image shuffling / re-shuffling process (substitution)
x: Initial Condition
r: Control Parameter
n: Number of keys to be generated
"""
def indexgen(x, r, n): #Optimized -> O(n log n)
    index = []
    k = []

    for i in range(n):
        x = r * x * (1 - x) # Logistic Map
        k.append(int((x * pow(10, 16)) % 256))
        # k.append(x) # Generating the key
        index.append(i) # Generating the index

    zipped = zip(k, index) # Zip the two lists together
    sorted_zipped = sorted(zipped) # Sort the zipped list
    sorted_k, sorted_index = zip(*sorted_zipped) # Unzip the sorted list back into separate lists

    return sorted_index
