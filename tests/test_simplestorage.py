from brownie import accounts, config, SimpleStorage

def test_retrive():
    #Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})

    #Act
    expected =0
    value = simple_storage.retrieve()
    assert expected == value
def test_updating_storage():
    #Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})

    #Act
    expected =15
    simple_storage.store(15,{"from": account})
    assert expected == simple_storage.retrieve()




