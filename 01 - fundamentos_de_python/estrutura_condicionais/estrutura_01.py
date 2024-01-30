saldo = 2000.0
saque = float(input("Informe o valor do saque: R$ "))

if saldo >= saque:
    print("\nSaque realizado!\n")
else:
    print("\nSaldo insulficiente!\n")

saldo -= saque

print(f"Saldo atual: R$ {saldo:.2f} reais.\n")