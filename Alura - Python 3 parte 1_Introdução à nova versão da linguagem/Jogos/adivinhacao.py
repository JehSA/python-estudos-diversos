
print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
totalTentativas = 3
rodada = 1

while(rodada <= totalTentativas):
    print("Tentativa {} de {}".format(rodada, totalTentativas))

    chute_str = input("Digite o seu palpite: ")

    print("Voce digitou ", chute_str)

    chute = int(chute_str)

    acertou = numero_secreto == chute
    maior = numero_secreto < chute
    menor = numero_secreto > chute

    if(acertou):
        print("Você Acertou!")
    elif(maior):
        print("Você errou! O seu chute foi maior do que o número secreto.")
    elif(menor):
        print("Você errou! O seu chute foi menor do que o número secreto.")

    rodada = rodada + 1

print("Fim do jogo!!!")



#print(type(chute))
#print(type(numero_secreto))