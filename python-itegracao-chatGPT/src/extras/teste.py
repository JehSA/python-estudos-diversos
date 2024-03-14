import cowsay
import random

def console_divertido(texto):
    funcoes = [
        cowsay.tux,
        cowsay.cow,
        cowsay.turtle,
        cowsay.dragon
    ]

    funcao = random.choice(funcoes)
    funcao(texto)


console_divertido("Olá python!!!")