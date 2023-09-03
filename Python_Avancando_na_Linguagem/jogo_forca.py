import random

def jogar():
    load_main_menu()
    palavra_secreta = load_secret_word(nome_arquivo="frutas.txt", primeira_linha_valida=0)
    letras_acertadas = load_view_prompt_letters(palavra_secreta) #utilizando list compreensions

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    #enquanto for true
    while(not enforcou and not acertou):

        chute = prompt_guess_letters()

        if(chute in palavra_secreta):
            load_letter_guess_prompt(chute, palavra_secreta, letras_acertadas)
            
        else:
            erros += 1
            desenha_forca(erros)
        
        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        load_win_message()
    else:
        load_game_over_message(palavra_secreta)



def load_main_menu():
    print("*********************************")
    print("Bem vindo no jogo de Forca!")
    print("*********************************")

def load_secret_word(primeira_linha_valida = 0, nome_arquivo = "palavras.txt"):
    arquivo = open(nome_arquivo, "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(primeira_linha_valida,len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta

def load_view_prompt_letters(palavra):
    return ["_" for letra in palavra] #utilizando list compreensions

def prompt_guess_letters():
    chute = input("Chute uma letra !?")
    chute = chute.strip().upper()
    return chute

def load_letter_guess_prompt(chute, palavra_secreta, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if (chute.upper() == letra.upper()):
            letras_acertadas[index] = letra
        index += 1 #iterador do loop

def load_win_message():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def load_game_over_message(palavra_secreta):
    print("GAME OVER!!! Você perdeu!!!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
    
def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__=="__main__"):
    jogar()

