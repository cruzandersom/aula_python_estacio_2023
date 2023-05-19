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
        if self.__saldo >= valor:
            self.__saldo -= valor
        else:
            print("Não foi possível realizar o saque\nSaldo insuficiente")

    def transfere(self, valor: float, destino):
        self.saca(valor)
        destino.deposita(valor)

    def extrato(self) -> None:
        print("Saldo de {} do titular {}".format(self.__saldo, self.titular))


    def get_saldo(self) -> float:
        return self.__saldo

    def set_saldo(self, saldo: float) -> None:
        self.__saldo = saldo