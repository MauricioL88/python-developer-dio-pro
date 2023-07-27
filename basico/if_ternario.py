LIMITE_SAQUE = 300.00

saque = float(input("Qual valor que deseja sacar?: R$ "))

def sacar(valor):
    saldo = 2000.00
    if (valor <= saldo) and (valor <= LIMITE_SAQUE):
        saldo -= valor
        return saldo

status = f"\nSaque: R$ {saque} | Saldo: R$ {sacar(saque)}" if saque <= LIMITE_SAQUE else "Valor de saque excedido!\n"

print(status)