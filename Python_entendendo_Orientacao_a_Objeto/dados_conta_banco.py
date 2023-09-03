from teste import create_account, account_deposit, account_withdraw, account_statement

#Simulando dados de uma conta
account_number = 123
account_owner = "Lucas Dipré Pereira"
account_balance = 55.0
account_limit = 1000

#Criando no formato de um dicionário
dict_conta = {
        "account_number": 123, 
        "account_owner": "Nico", 
        "account_balance": 55.0, 
        "account_limit": 1000.0
        }

created_account = create_account(7685945, "Lucas Dipré", 200.0, 1000.0)

account_deposit(created_account, 20)
account_statement(created_account)
account_withdraw(created_account, 40)
account_statement(created_account)

# O problema vai aparecer e persistir ao trabalhar com diversar contas, 
# e que não tenham todas essas caracteristicas