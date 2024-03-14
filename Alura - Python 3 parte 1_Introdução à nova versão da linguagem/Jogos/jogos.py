import forca
import adivinhacaoFor

print("*********************************")
print("******Escolha o seu jogo*********")
print("*********************************")

print("(1) Forca   (2) Adivinhação")

jogo = int(input("Digite a opção: "))

if(jogo == 1):
    print("Você escolheu o jogo da Forca!")
    forca.jogar()
elif(jogo == 2):
    print("Você escolheu o jogo da Adivinhação!")
    adivinhacaoFor.jogar()

