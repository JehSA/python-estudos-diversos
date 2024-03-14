class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite


    def getExtrato(self):
        print("O seu saldo é {}", self.saldo)


    def saca(self, valor):
        self.saldo -= valor


    def deposita(self, valor):
        self.saldo += valor


    def transferir(self, pessoa, valor):
        self.saca(valor)
        pessoa.deposita(valor)


conta1 = Conta(123, "Jefferson", 55.5, 1000.0)
conta2 = Conta(123, "Levi", 155.5, 2000.0)

print(conta1.saldo)

conta1.saca(10)
conta1.deposita(210)

conta1.transferir(conta2, 20.0)

conta1.getExtrato()
conta2.getExtrato()