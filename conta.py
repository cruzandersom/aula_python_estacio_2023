class Conta:

    def __init__(self, titular: str, numero: int,
                 saldo: float, limite: float):
        self.__titular: str = titular
        self.__numero: int = numero
        self.__saldo: float = saldo
        self.__limite: float = limite

    def deposita(self, valor: float) -> None:
        self.__saldo += valor

    def saca(self, valor: float) -> None:
        if self.__pode_sacar(valor):
            self.__saldo -= valor
            print("Saque realizado com sucesso")
        else:
            print("Não foi possível realizar o saque\nSaldo insuficiente")

    def __pode_sacar(self, valor: float) -> bool:
        return self.__saldo >= valor

    def transfere(self, valor: float, destino):
        self.saca(valor)
        destino.deposita(valor)

    def extrato(self) -> None:
        print("Saldo de {} do titular {}".format(self.__saldo, self.titular))

    @property
    def saldo(self) -> float:
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo: float) -> None:
        self.__saldo = saldo
