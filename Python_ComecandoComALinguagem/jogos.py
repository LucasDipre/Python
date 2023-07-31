import jogo_forca
import jogo_adivinhacao

def escolher_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo*******")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo?"))
    if(jogo == 1):
        print("Jogando forca !")
        jogo_forca.jogar()
    elif(jogo == 2):
        print("Jogando Adivinhação !")
        jogo_adivinhacao.jogar()

if(__name__=="__main__"):
    escolher_jogo()
