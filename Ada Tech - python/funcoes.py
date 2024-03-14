def saudacao():
    print('Olá! Seja bem vindo(a)!')
    print('Teste 2...')
saudacao()
saudacao()

def saudacao2(nome, variavel2):
    print(f'Olá! Seja bem vindo(a), {nome}!')
    print(f'Teste 2..., {variavel2}')
saudacao2('Jefferson', 'Alô! Variável 2!!!!!')

def saudacao2(nome, variavel2 = 'Python'):
    print(f'Olá! Seja bem vindo(a), {nome}!')
    print(f'Teste 2..., {variavel2}')
saudacao2('Jefferson', 'JavaScript')


# Funções c/ retorno
def soma(num1, num2):
    return int(num1 + num2)
resultado = soma(1, 3)
print(resultado)


# Exemplo
def calculator(num1, num2, operacao = '+'):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
resultado = calculator(10, 20)
print(resultado)
resultado2 = calculator(10, 20, '-')
print(resultado2)
