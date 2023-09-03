#Possivel jeito de criar classes em usar OO em procedural
def create_account(account_number, account_owner, account_balance,account_limit):
    dict_account = {
        "account_number": account_number, 
        "account_owner": account_owner, 
        "account_balance": account_balance, 
        "account_limit": account_limit
        }
    return dict_account

def account_deposit(dict_account, value):
    dict_account["account_balance"] += value

def account_withdraw(dict_account,value):
    dict_account["account_balance"] -= value

def account_statement(dict_account):
    print("Saldo é {}".format(dict_account["account_balance"]))