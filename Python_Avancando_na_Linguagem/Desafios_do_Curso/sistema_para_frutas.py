# Mariana montou o seguinte código Python para controlar se a sua barraca 
# de frutas possui determinadas frutas solicitadas pelos seus clientes:

# coding: utf-8
frutas = ['Banana', 'Maçã', 'Pera', 'Uva', 'Melancia', 'Jamelão']

fruta_pedida = input('Qual é a fruta que deseja consultar ?')

#o desafio era completar o condicional do if com o comando correto
if(fruta_pedida in frutas):
    print ('Sim, temos a fruta.')
else:
    print ('Não temos a fruta.')