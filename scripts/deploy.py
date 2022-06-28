from brownie import accounts, network, FundMe
from scripts.helpful_scripts import get_account


def deploy_fund_me():
    account = get_account()
    print(account)
    fund_me = FundMe.deploy(account,{"from":account})
    #print(f"Contract deployed to {fund_me.address}")
    

def main():
    deploy_fund_me()