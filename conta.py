

class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite


    def extrato(self):
        print("Sr(a). {}, o seu saldo é de R$ {} .".format(self.__titular, self.__saldo))

    def deposito(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_saque):
        disponivelSaque = self.__saldo + self.limite
        return valor_saque <= disponivelSaque

    def saque(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("Você não possui saldo ou limite suficiente para esta operção.")

    def transferencia(self, valor, destino):
        self.saque(valor)
        destino.deposito(valor)

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}

