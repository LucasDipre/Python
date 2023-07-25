print("*********************************")
print("Bem vindo no jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 3


for rodada in range (1, total_de_tentativas + 1): # + 1 pois o segundo parametro é exclusivo
    print("Tentativa {} de {}:".format(rodada, total_de_tentativas))#Interpolação de String

    chute_str = input("Digite o número entre 1 e 100: ") #conversão não feita para int sempre dará erro

    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("Digite um número entre 1 e 100:")
        continue # refaz a interação do for até o if novamente

    print("Você digitou ", chute_str)

    acertou = chute == numero_secreto
    chute_foi_maior = chute > numero_secreto
    chute_foi_menor = chute < numero_secreto

    if(acertou): 
        print("Você acertou!")
        break  # sai do laço e não constinua o código até o fim do for
    else:
        if(chute_foi_maior):
            print("Você errou! O seu numero foi maior do que o numero secreto!")
        elif(chute_foi_menor):
            print("Você errou! O seu numero foi menor do que o numero secreto!")

    rodada = rodada + 1

print("Fim do Jogo!")