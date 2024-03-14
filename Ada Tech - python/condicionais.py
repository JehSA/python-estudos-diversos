# Exemplo 1
idade = int(input('Digite a sua idade:'))
if idade >= 18:
    print('Você é maior de idade!')
else:
    print('Você é menor de idade')

# Exemplo 2
nota1 = float(input('Digite a nota 1:'))
nota2 = float(input('Digite a nota 2:'))
presenca = int(input('Digite a presenca:'))
media = (nota1 + nota2) / 2
if media >= 7 and presenca > 70:
    print('Você é foi aprovado!')
elif media >= 5 and presenca > 70:
    print('Você está de recuperação!')
else:
    print('Você foi reprovado!')