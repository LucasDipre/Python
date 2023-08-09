#Gera uma lista filtrando de uma outra lista os nuemros pares
inteiros = [1,3,4,5,7,8,9]
pares = []
for numero in inteiros:
    if numero % 2 == 0:
        pares.append(numero)
#o mesmo código em list compreehensions fica:
inteiros = [1,3,4,5,7,8,9]
pares = [x for x in inteiros if x % 2 == 0]
########################################################

inteiros = [1,3,4,5,7,8]
#preencher uma nova lista com o quadrado de cada número da lista anterior
inteiros = [1,3,4,5,7,8]

########################################################
frutas = ["maçã", "banana", "laranja", "melancia"]
#Agora ele precisa criar uma nova lista com as mesmas frutas, 
# mas tudo escrito em letras maiúsculas. Ele escreveu o laço abaixo:
#sem list comprehensions
lista = []
for fruta in frutas:
    lista.append(fruta.upper())
#Com list Comprehensions
lista = [fruta.upper() for fruta in frutas]