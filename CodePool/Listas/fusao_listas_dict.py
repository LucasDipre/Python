#código que pega duas listas de strings e combina em um dicionário
lista_de_compras = ['arroz', 'feijao', 'macarrao']
preco_dos_itens = ['2.00', '3.80', '4.90']
dict = {}
for i,j in zip(lista_de_compras, preco_dos_itens):
    dict[i] = j
print(dict) 