# Exemplo 1
numero_sorteado = 15

numero_escolhido = int(input('Informe um numero entre 1 e 20:'))

while numero_sorteado != numero_escolhido:
    print('Você errou!! Tente novamente...')
    numero_escolhido = int(input('Informe um numero entre 1 e 20:'))
    if numero_escolhido == numero_sorteado:
        print('Você acertou!')


# Exemplo 2 - Contador
contador = 0

while contador <= 5:
    print(contador)
    contador = contador + 1