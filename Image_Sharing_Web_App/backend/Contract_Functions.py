#API DEFINITION
from web3 import Web3, HTTPProvider

def web3_init(infura_endpoint_base, infura_project_id,abi,contract_address):
  
  w3 = Web3(HTTPProvider(infura_endpoint_base + infura_project_id))
  contract = w3.eth.contract(address=contract_address, abi=abi)
  return w3, contract



def getMerkleRootHash(contract,user_id,image_id):
  return contract.functions.get(user_id,image_id).call()


  
def setMerkleRootHash(web3, contract, acct_private_key, user_id,hash_value):

  account = web3.eth.account.privateKeyToAccount(acct_private_key)

  # Create a transaction object
  nonce = web3.eth.getTransactionCount(account.address)
  gas_price = web3.eth.gasPrice
  gas_limit = 500000
  tx = contract.functions.set(user_id,hash_value).buildTransaction({
      "from": account.address,
      "nonce": nonce,
      "gasPrice": gas_price,
      "gas": gas_limit
  })

  # Sign the transaction with the account's private key
  signed_tx = account.signTransaction(tx)

  # Send the signed transaction to the network
  tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

  receipt = web3.eth.waitForTransactionReceipt(tx_hash)
  print(receipt)
    

def registerUser(web3, contract, acct_private_key, user_id,first_name,last_name):
  account = web3.eth.account.privateKeyToAccount(acct_private_key)

  # Create a transaction object
  nonce = web3.eth.getTransactionCount(account.address)
  gas_price = web3.eth.gasPrice
  gas_limit = 500000
  tx = contract.functions.insert_user(user_id,first_name,last_name).buildTransaction({
      "from": account.address,
      "nonce": nonce,
      "gasPrice": gas_price,
      "gas": gas_limit
  })

  # Sign the transaction with the account's private key
  signed_tx = account.signTransaction(tx)

  # Send the signed transaction to the network
  tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

  receipt = web3.eth.waitForTransactionReceipt(tx_hash)
  print(receipt)


def doesUserExist(contract, user_id):
  return contract.functions.check_user(user_id).call()


def grantAccess(web3, contract, acct_private_key, sender, receiver,idx):
  account = web3.eth.account.privateKeyToAccount(acct_private_key)

  # Create a transaction object
  nonce = web3.eth.getTransactionCount(account.address)
  gas_price = web3.eth.gasPrice
  gas_limit = 500000
  tx = contract.functions.grant_access(sender,receiver,idx).buildTransaction({
      "from": account.address,
      "nonce": nonce,
      "gasPrice": gas_price,
      "gas": gas_limit
  })

  # Sign the transaction with the account's private key
  signed_tx = account.signTransaction(tx)

  # Send the signed transaction to the network
  tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

  receipt = web3.eth.waitForTransactionReceipt(tx_hash)
  print(receipt)
  return receipt


def revoke_access(web3, contract, acct_private_key, sender, receiver,idx):
  account = web3.eth.account.privateKeyToAccount(acct_private_key)

  # Create a transaction object
  nonce = web3.eth.getTransactionCount(account.address)
  gas_price = web3.eth.gasPrice
  gas_limit = 500000
  tx = contract.functions.revoke_access(sender,receiver,idx).buildTransaction({
      "from": account.address,
      "nonce": nonce,
      "gasPrice": gas_price,
      "gas": gas_limit
  })

  # Sign the transaction with the account's private key
  signed_tx = account.signTransaction(tx)

  # Send the signed transaction to the network
  tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

  receipt = web3.eth.waitForTransactionReceipt(tx_hash)
  print(receipt)
  return(receipt)


def shareImage(web3, contract, acct_private_key, sender, receiver, url, image_hash, time_stamp,caption):
  print("Hi")
  account = web3.eth.account.privateKeyToAccount(acct_private_key)
  print("Hi")
  # Create a transaction object
  nonce = web3.eth.getTransactionCount(account.address)
  gas_price = web3.eth.gasPrice
  gas_limit = 1000000
  tx = contract.functions.add_image_details(sender,receiver,url,image_hash,time_stamp,caption).buildTransaction({
      "from": account.address,
      "nonce": nonce,
      "gasPrice": gas_price,
      "gas": gas_limit
  })

  # Sign the transaction with the account's private key
  signed_tx = account.signTransaction(tx)

  # Send the signed transaction to the network
  tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

  receipt = web3.eth.waitForTransactionReceipt(tx_hash)
  print(receipt)


def getSharedImages(contract, acct_private_key, sender, receiver):
  return contract.functions.get_images_shared(sender,receiver).call()


def getNames(contract, acct_private_key, user):
  return contract.functions.get_Names(user).call()





