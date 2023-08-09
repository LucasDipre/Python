import random

def jogar():
    print("*********************************")
    print("Bem vindo no jogo de Forca!")
    print("*********************************")

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()

    letras_acertadas = ["_" for letra in palavra_secreta] #utilizando list compreensions

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    #enquanto for true
    while(not enforcou and not acertou):

        chute = input("Chute uma letra !?")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute.upper() == letra.upper()):
                    letras_acertadas[index] = letra
                index += 1 #iterador do loo
        else:
            erros += 1
            print("Ops, você errou! Faltam {} tentativas.".format(6-erros))
        
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        print("Você ganhou!")
    else:
        print("Você perdeu!")

    print("Fim do Jogo!")

if(__name__=="__main__"):
    jogar()

