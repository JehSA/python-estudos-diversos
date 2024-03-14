import random

def abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def carregaPalavraSecreta():
    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavraSecreta = palavras[numero].upper()
    return palavraSecreta

def inicializaLetrasAcertadas(palavra):
    return ["_" for letra in palavra]

def pedeChute():
    chute = input("Digite uma letra: ")
    chute = chute.strip().upper()
    return chute

def marcaChuteCorreto(chute, letrasAcertadas, palavraSecreta):
    index = 0
    for letra in palavraSecreta:
        if (chute == letra):
            letrasAcertadas[index] = letra
        index = index + 1

def mensagemVencedor():
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

def mensagemPerdedor(palavraSecreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavraSecreta))
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


def jogar():

    abertura()
    palavraSecreta = carregaPalavraSecreta()
    letrasAcertadas = inicializaLetrasAcertadas(palavraSecreta)

    print(letrasAcertadas)

    enforcou = False
    acertou = False
    erros = 0
    
    while(not enforcou and not acertou):

        chute = pedeChute()

        if(chute in palavraSecreta):
            marcaChuteCorreto(chute, letrasAcertadas, palavraSecreta)
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letrasAcertadas

        print(letrasAcertadas)

    if(acertou):
        mensagemVencedor()
    else:
        mensagemPerdedor(palavraSecreta)


    print("Fim do jogo!!!")




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



if(__name__ == "__main__"):
    jogar()