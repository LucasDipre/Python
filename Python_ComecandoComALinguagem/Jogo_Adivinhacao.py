print("*********************************")
print("Bem vindo no jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

chute_str = input("Digite o numero: ")
#Se não for feita aqui a conversão para int sempre dará erro
chute = int(chute_str)

print("Você digitou ", chute_str)

acertou = chute == numero_secreto
chute_foi_maior = chute > numero_secreto
chute_foi_menor = chute < numero_secreto

if(acertou): 
    print("Você acertou!")
else:
    if(chute_foi_maior):
        print("Você errou! O seu numero foi maior do que o numero secreto!")
    elif(chute_foi_menor):
        print("Você errou! O seu numero foi menor do que o numero secreto!")

print("Fim do Jogo!")