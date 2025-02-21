class cuentabancaria:
    def __init__(self, monto):
        self.monto = monto
    def depositar(self, monto):
        self.monto += monto
    def retirar(self, monto):
        self.monto -= monto
    def ver_saldo(self):
        return f"El saldo es de {self.monto} €"
s = cuentabancaria(1000)
s.depositar(500)
s.retirar(300)
print(s.ver_saldo())