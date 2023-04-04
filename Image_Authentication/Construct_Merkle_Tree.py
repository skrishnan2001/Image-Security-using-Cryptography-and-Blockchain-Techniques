import hashlib
import io
from PIL import Image

def hash_data(data):
    hash_object = hashlib.sha256(str(data).encode('utf-8'))
    return hash_object.hexdigest()

def get_image_chunks(image, chunk_size=128):
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

def get_leaves(chunks):
    leaves = []
    for chunk in chunks:
        leaves.append(hash_data(chunk))
    return leaves


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
    image_file_name = 'disneyland-paris'
    ext = '.jpg'
    complete_file_path = image_directory_path + image_file_name + ext
    print('Image File path: ', complete_file_path)
    with open(complete_file_path, 'rb') as f:
        image = f.read()
        chunks = get_image_chunks(image)
        print("Number of chunks: ", len(chunks))
        print("Hash of leaf nodes: ", get_leaves(chunks), "\n")
        root = construct_merkle_tree(chunks)
        print("Root Hash:", root)
