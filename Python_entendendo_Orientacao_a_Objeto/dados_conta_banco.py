from teste import create_account, account_deposit, account_withdraw, account_statement
from conta import Account

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

#Utilizando a classe conta, retorna a posição de memória em que o objetyo foi criado
#print(Account()) # Começa a dar erro pois não estou mais passando os parâmetros

#Guardando o objeto dentro de uma váriável refrência
# account = Account() # Começa a dar erro pois não estou mais passando os parâmetros
# print(account)

#Após criar os atributos da classe criamos
banck_account = Account(12342345, "Lucas", 60.0)
banck_account2 = Account(12342345, "Carvalhosa", 90.0, 2000.0)

#Acessando os Objetos das contas criadas
print(banck_account)
print(banck_account2)
print(banck_account.account_balance)
print(banck_account.account_limit)
print(banck_account2.account_balance)
print(banck_account2.account_limit)