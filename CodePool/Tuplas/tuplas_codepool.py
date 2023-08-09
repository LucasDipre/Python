#Tuplas são listas que não mudam, mais fixas
dias = ("Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado")

print(type(dias))
print(len(dias))

#pontos de um gráfico
ponto = (3,5)
print(ponto)

p1 = (3,5)
p2 = (4,6)
p3 = (5,7)

line = [p1, p2, p3]

print(line)

#instrutores
instrutor1 = ("Nico", 39)
instrutor2 = ("Flávio", 37)

instrutores = [instrutor1, instrutor2]

print(instrutores[0])

print(instrutores[0][1])

#lendo de um arquivo pois ele é uma lista de strings
linhas_palavras = []
linhas_palavras.append("banana")
linhas_palavras.append("abacaxi")
linhas_palavras.append("laranja")

nova = tuple(linhas_palavras)

print(nova)
print(type(nova))

outra = list(nova)

print(outra)
print(type(outra))

