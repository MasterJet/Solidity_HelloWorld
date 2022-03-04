from brownie import accounts, HelloWorld


def deployHelloWorld():
    hello_world = HelloWorld.deploy("Hello World", {"from": accounts[0]})
    print("Contract Deployed ...")
    initialMessage = hello_world.GetMessage()
    print(f"Initial Message is [{initialMessage}]")
    print("Updating Message ...")
    hello_world.UpdateMessage("Hello Solidity", {"from": accounts[0]})
    UpdatedMessage = hello_world.GetMessage()
    print(f"Updated Message is now [{UpdatedMessage}]")


def main():
    deployHelloWorld()
