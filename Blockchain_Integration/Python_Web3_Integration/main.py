from Merkle_Root_Getter_Setter import (
    web3_init,
    setMerkleRootHash,
    getLatestMerkleRootHash,
)
import json
import os
from dotenv import load_dotenv
import sys

sys.path.append("../../")
from Image_Authentication.Construct_Merkle_Tree import (
    construct_merkle_tree,
    get_image_chunks,
    get_leaves,
)


if __name__ == "__main__":
    with open("HashStorage.json") as f:
        info_json = json.load(f)
    abi = info_json["abi"]

    load_dotenv()

    contract_address = os.getenv("CONTRACT_ADDRESS")
    infura_project_id = os.getenv("INFURA_PROJECT_ID")
    infura_endpoint = os.getenv("INFURA_ENDPOINT")
    acct_private_key = os.getenv("ACCT_PRIVATE_KEY")

    web3, contract = web3_init(
        infura_endpoint, infura_project_id, abi, contract_address
    )

    # Getting value from contract
    sample_user = "skrishnan2001"

    # Getting the hash of encrypted image
    image_directory_path = "Images/"
    image_file_name = "Au_ani_00001"
    ext = ".jpg"
    complete_file_path = image_directory_path + image_file_name + ext
    print("Image File path: ", complete_file_path)
    with open(complete_file_path, "rb") as f:
        image = f.read()
        chunks = get_image_chunks(image)
        print("Number of chunks: ", len(chunks))
        print("Hash of leaf nodes: ", get_leaves(chunks), "\n")
        image_hash = construct_merkle_tree(chunks)
        print("Root Hash:", image_hash)

    # Updating the value
    setMerkleRootHash(web3, contract, acct_private_key, sample_user, image_hash)

    # Retrieving the updated value
    hash_value = getLatestMerkleRootHash(contract, sample_user)

    print("Hash value for the latest image belonging to user ID ", sample_user, " is ",hash_value)
