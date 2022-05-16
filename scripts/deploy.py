from brownie import accounts, config, SimpleStorage,network
import os
#0xF071265ac4c12526ee30ba2Dc57791CC12a248b7
def deploy_simple_storage():
    #account = accounts.add(os.getenv(""))
    account = accounts.add(config["wallets"]["key"])
    simple_storage = SimpleStorage.deploy({"from":account})
    value = simple_storage.retrieve()
    print(value)
    transac = simple_storage.store(15,{"from":account})
    transac.wait(1)
    svalue = simple_storage.retrieve()
    print(svalue)

    print(account)

def getaccount():
    if(network.show_active()== "development"):
        account = accounts[0]
        return account
    else:
        account = accounts.add(config["wallets"]["key"])
        return account

def main():
    deploy_simple_storage()