class Conta:

    def __init__(self, titular: str, numero: int,
                 saldo: float, limite: float):
        self.titular: str = titular
        self.numero: int = numero
        self.saldo: float = saldo
        self.limite: float = limite
        print("Minha classe")

    def deposita(self, valor: float) -> None:
        self.saldo += valor

    def saca(self, valor: float) -> None:
        self.saldo -= valor

    def extrato(self) -> None:
        print("Saldo de {} do titular {}".format(self.saldo, self.titular))
