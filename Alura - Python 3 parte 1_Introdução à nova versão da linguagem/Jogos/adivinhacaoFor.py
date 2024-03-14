import random

def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    totalTentativas = 0
    pontos = 1000
    #print(numero_secreto)

    print("Selecione o nível de dificuldade...")
    print("(1) Fácil  (2) Médio  (3) Difícil")

    nivel = int(input("Digite o nível: "))

    if(nivel == 1):
        totalTentativas = 20
    elif(nivel == 2):
        totalTentativas = 103
    else:
        totalTentativas = 5


    for rodada in range(1, totalTentativas + 1):
        print("Tentativa {} de {}".format(rodada, totalTentativas))

        chute_str = input("Digite o seu palpite entre 1 e 100: ")

        print("Voce digitou ", chute_str)

        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100.")
            continue

        acertou = numero_secreto == chute
        maior = numero_secreto < chute
        menor = numero_secreto > chute

        if(acertou):
            print("Você Acertou! Fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior do que o número secreto.")
            elif(menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")

            pontosPerdidos = abs(numero_secreto - chute)
            pontos = pontos - pontosPerdidos


    print("Fim do jogo!!!")

if (__name__ == "__main__"):
    jogar()

    #print(type(chute))
    #print(type(numero_secreto))