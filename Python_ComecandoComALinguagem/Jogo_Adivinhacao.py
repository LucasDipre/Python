print("*********************************")
print("Bem vindo no jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while (rodada <= total_de_tentativas):
    print("Tentativa {} de {}:".format(rodada, total_de_tentativas))#Interpolação de String

    chute_str = input("Digite o numero: ") #conversão não feita para int sempre dará erro

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

    rodada = rodada + 1
    print("Fim do Jogo!")