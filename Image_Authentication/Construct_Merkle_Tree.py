import hashlib
import io
from PIL import Image

def hash_data(data):
    hash_object = hashlib.sha256(str(data).encode('utf-8'))
    return hash_object.hexdigest()

def get_image_chunks(image, chunk_size=1024):
    img = Image.open(io.BytesIO(image))
    width, height = img.size
    chunks = []
    for y in range(0, height, chunk_size):
        for x in range(0, width, chunk_size):
            block = img.crop((x, y, x + chunk_size, y + chunk_size))
            chunk = io.BytesIO()
            block.save(chunk, format='JPEG')
            chunks.append(chunk.getvalue())
    return chunks

def construct_merkle_tree(chunks): #Recursive Function
    if len(chunks) == 1:
        return hash_data(chunks[0])
    if len(chunks) % 2 == 1:
        chunks.append(chunks[-1])
    parent_level = []
    for i in range(0, len(chunks), 2):
        parent = hash_data(chunks[i] + chunks[i+1])
        parent_level.append(parent)
    return construct_merkle_tree(parent_level)

if __name__ == '__main__':
    image_directory_path = 'Images/'
    image_file_name = 'ISTDept_EncryptedImage'
    ext = '.jpg'
    complete_file_path = image_directory_path + image_file_name + ext
    print('Image File path: ', complete_file_path)
    with open(complete_file_path, 'rb') as f:
        image = f.read()
        chunks = get_image_chunks(image)
        root = construct_merkle_tree(chunks)
        print("Root Hash:", root)
