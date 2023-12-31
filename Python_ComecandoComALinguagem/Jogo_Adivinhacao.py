import random

def jogar():

    print("*********************************")
    print("Bem vindo no jogo de Adivinhação!")
    print("*********************************")

    #Gera um numero randomico, arredonda e transforma em int
    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 3
    pontos = 1000

    #Inclui níveis ao jogo baseado no total de tentativas
    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    #Roubando para testar o numero randomico secreto
    print("Roubando: ", numero_secreto)

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
            print("Você acertou e fez {} pontos!".format(pontos))
            break  # sai do laço e não constinua o código até o fim do for
        else:
            dano = abs(numero_secreto - chute) 
            pontos = pontos - dano
            if(chute_foi_maior):
                print("Você errou! O seu numero foi maior do que o numero secreto!")
                if (rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))  
            elif(chute_foi_menor):
                print("Você errou! O seu numero foi menor do que o numero secreto!")
                if (rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {}".format(
                        numero_secreto, pontos))

        rodada = rodada + 1

    print("Fim do Jogo!")

if(__name__=="__main__"):
    jogar()

