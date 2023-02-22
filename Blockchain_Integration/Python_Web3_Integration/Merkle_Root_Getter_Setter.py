from web3 import Web3, HTTPProvider


def web3_init(infura_endpoint_base, infura_project_id, abi, contract_address):
    w3 = Web3(HTTPProvider(infura_endpoint_base + infura_project_id))
    contract = w3.eth.contract(address=contract_address, abi=abi)
    return w3, contract


def getMerkleRootHash(contract, user_id, image_id):
    return contract.functions.get(user_id, image_id).call()


def getLatestMerkleRootHash(contract, user_id):
    return contract.functions.get_latest_hash(user_id).call()


def setMerkleRootHash(web3, contract, acct_private_key, user_id, hash_value):
    account = web3.eth.account.privateKeyToAccount(acct_private_key)

    # Create a transaction object
    nonce = web3.eth.getTransactionCount(account.address)
    gas_price = web3.eth.gasPrice
    gas_limit = 500000
    tx = contract.functions.set(user_id, hash_value).buildTransaction(
        {
            "from": account.address,
            "nonce": nonce,
            "gasPrice": gas_price,
            "gas": gas_limit,
        }
    )

    # Sign the transaction with the account's private key
    signed_tx = account.signTransaction(tx)

    # Send the signed transaction to the network
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

    receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    print(receipt)
