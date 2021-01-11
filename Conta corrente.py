class CC:
    def __init__(self, pTitular, pNumero, pSaldo, pLimite = 0):
        self.titular = pTitular
        self.numero = pNumero
        self.saldo = pSaldo
        self.limite = pLimite

    def sacar(self, saque):
        if (self.saldo + self.limite >= saque):
            self.saldo -= saque
        else:
            print("---")

    def depositar(self,deposito):
        self.saldo += deposito

    def pagar(self, valor):
        self.saldo -= valor

CCValeria = CC("valeria", 12345, 200)
CCBia = CC("Bia", 54321, 700)
CCValeria.pagar(450)
CCBia.sacar(225)
CCValeria.depositar(225)