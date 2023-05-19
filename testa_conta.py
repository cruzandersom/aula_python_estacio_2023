from conta import Conta

conta = Conta('João', 123, 55.5, 1000.0)
print(conta)

conta = Conta('João', 123, 55.5, 1000.0)
print(conta)

print(f"Esse é o saldo da conta {conta.get_saldo()}")

conta.deposita(100.0)

print(f"Esse é o saldo da conta{conta.get_saldo()}")
