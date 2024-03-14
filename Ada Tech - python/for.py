for variavel in range(10):
    print('Olá', variavel)

for variavel in range(3, 11):
    print('Teste range...', variavel)

for variavel in range(1, 12, 3):
    print('pulando de 3 em 3', variavel)

# Exemplo 1
soma = 0

for i in range(1, 4):
    nota = float(input(f'Digite nota {i}:'))
    soma = soma + nota

print(f'Sua média é {soma / 3}!')
