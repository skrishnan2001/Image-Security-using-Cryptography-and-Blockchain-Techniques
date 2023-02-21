from brownie import HashStorage, accounts
def main():
    account = accounts.load('deployment_account')
    HashStorage.deploy({'from': account})