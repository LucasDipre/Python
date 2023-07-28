# O professor Flávio tem o costume de sortear um livro da Casa do Código ao final 
# de todos os seus cursos para os seus 3 melhores alunos. Desta vez, os três 
# melhores alunos foram:

# Paulo
# Juliana
# Tamires

# Quando executado o script foi anunciado que a Tamires era a vencedora, porém Paulo 
# após conferir o código exclamou que o sorteio não era justo e que ele e a Juliana 
# tinham menos de chances de ganhar!

# De acordo com seus conhecimentos de Python, analise o código acima e avalie se o 
# sorteio foi justo ou não e dê uma justificativa para tal!

import random

sorteado = random.randrange(0,4) # integer from 0 to 4 inclusive

print(sorteado)

if sorteado == 1:
    print( "Paulo")
elif sorteado == 2:
    print("Juliana")
else:
    print("Tamires")


# O sorteio foi injusto, afinal os possíveis números retornados são 0, 1, 2 e 3 ,
# e como o Paulo e a Juliana estão associadas a apenas um número cada sobram 
# ainda outros dois para Tamires poder ganhar.