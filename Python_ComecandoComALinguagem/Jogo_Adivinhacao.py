print("*********************************")
print("Bem vindo no jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

chute_str = input("Digite o numero: ")
#Se não for feita aqui a conversão para int sempre dará erro
chute = int(chute_str)

print("Você digitou ", chute_str)

if(numero_secreto == chute): 
    print("Você acertou!")
else:
    print("Você errou!")

print("Fim do Jogo!")