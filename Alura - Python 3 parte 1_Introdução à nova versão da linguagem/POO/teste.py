
def criarConta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

def deposito(conta, valor):
    conta["saldo"] += valor

def saque(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print("O seu saldo é: {}".format(conta["saldo"]))