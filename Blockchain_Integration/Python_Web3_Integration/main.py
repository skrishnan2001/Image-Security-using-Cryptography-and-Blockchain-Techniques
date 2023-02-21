from Merkle_Root_Getter_Setter import web3_init, getMerkleRootHash, setMerkleRootHash
import json
import os
from dotenv import load_dotenv

if __name__ == "__main__":
  
  with open("HashStorage.json") as f:
    info_json = json.load(f)
  abi = info_json["abi"]

  load_dotenv()

  contract_address = os.getenv('CONTRACT_ADDRESS')
  infura_project_id = os.getenv('INFURA_PROJECT_ID')
  infura_endpoint = os.getenv('INFURA_ENDPOINT')
  acct_private_key = os.getenv('ACCT_PRIVATE_KEY')


  web3, contract = web3_init(infura_endpoint, infura_project_id,abi,contract_address)

  #Getting value from contract
  sample_user = "skrishnan2001"
  sample_hash = "a286855f63aa50765faa5a60951b1229a33188ba40a306f9e52f7fca1b60e74c"
  

  #Updating the value 
  #setMerkleRootHash(web3, contract, acct_private_key, sample_user,sample_hash)

  #Retrieving the updated value
  idx = 1
  hash_value = getMerkleRootHash(contract,sample_user,idx)

  print("Hash value for image ID  ", idx, " belonging to user ID ", sample_user, " is ", hash_value) 
