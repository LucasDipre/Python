# Python exemples of program to print list
#Imprimindo listas
a = [1, 2, 3, 4, 5]

#usando for
for element in a :
    print(element)

#imprimindo a lista com os colchetes [1, 2, 3, 4, 5]
print(a)

# printing the list using * operator separated
# by comma
print(*a)

# printing the list using * and sep operator
print(*a, sep = ", ")

# print in new line
print(*a, sep = "\n")

# print the list by using list comprehension 
[print(i, end=' ') for i in a] #Com separador

[print(i) for i in a] #Sem separador

#l = [1,2,3,4,5,6]
#method 1
print(a[:])
 
#method 2
print(a[0:])
 
#method 3
print(a[0:len(a)])

valores = []

# imprime o tipo
print(type(valores))


### Acessasndo valores de listas de formas diferentes
valores = [0,1,2,3,4]

#imprime a lista toda
print(valores)

#imprimir valor minimo
print(min(valores))

#imprimir valor maximo
print(max(valores))

#imprime acessando uma posição da lista
print(valores[2])

#retorna true se o valor estiver na lista e fale se não estiver
print(0 in valores)

print(len(valores))

#imprime os elementos de uma lista acessando pelo index
numeros = [10, 20, 30, 40, 50]

for i in range(len(numeros)):
    print("O elemento na posição", i, "é", numeros[i])

#imprime as letras de uma frase acessando pleo index
frase = "Olá, mundo!"

for i in range(len(frase)):
    print("O caractere na posição", i, "é", frase[i])

#contar a quantidade de elementos x em uma lista
valores = [ 0, 0, 0, 1, 2, 3, 4]
print(valores.count(0))

# Utilizando a função .count() podemos por exemplo, 
# detectar quantas letras ainda faltam para o 
# nosso usuário preencher:
letras_acertadas = ['_','_','_','_','_','_']
letras_faltando = str(letras_acertadas.count('_'))
print( 'Ainda faltam acertar {} letras'.format(letras_faltando))

# Uma outra função que pode ser bastante útil é a função .index(), 
# que nos retorna o índice da primeira ocorrência de um determinado 
# elemento em uma lista, veja:
frutas = ['Banana', 'Morango', 'Maçã', 'Uva', 'Maçã', 'Uva']
print(frutas.index('Uva'))

# Não funciona quando o elemento não existe na lista
frutas = ['Banana', 'Morango', 'Maçã', 'Uva']

fruta_buscada = 'Melancia'
if fruta_buscada in frutas:
    print(frutas.index(fruta_buscada))
else:
    print('Desculpe, a {} não está na lista frutas'.format( fruta_buscada))





