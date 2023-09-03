
class Account:

    def __init__(self, account_number, account_owner, account_balance, account_limit = 1000.0): #Função construtora
        print("Construindo o objeto...")
        self.account_number = account_number
        self.account_owner = account_owner
        self.account_balance = account_balance
        self.account_limit = account_limit
