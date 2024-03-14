class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite


    def getExtrato(self):
        print("O seu saldo é {}", self.__saldo)


    def saca(self, valor):
        self.__saldo -= valor


    def deposita(self, valor):
        self.__saldo += valor


    def transferir(self, pessoa, valor):
        self.__saca(valor)
        pessoa.deposita(valor)


conta1 = Conta(123, "Jefferson", 55.5, 1000.0)
conta2 = Conta(123, "Levi", 155.5, 2000.0)

print(conta1.saldo)

conta1.saca(10)
conta1.deposita(210)

conta1.transferir(conta2, 20.0)

conta1.getExtrato()
conta2.getExtrato()