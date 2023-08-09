def jogar():
    print("*********************************")
    print("Bem vindo no jogo de Forca!")
    print("*********************************")

    palavra_secreta = "laranja"
    letras_acertadas = ["_", "_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False

    print(letras_acertadas)

    #enquanto for true
    while(not enforcou and not acertou):

        chute = input("Chute uma letra !?")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
            index = index + 1 #iterador do loop
        print(letras_acertadas)


    print("Fim do Jogo!")

if(__name__=="__main__"):
    jogar()

