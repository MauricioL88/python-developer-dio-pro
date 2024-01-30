saldo = 2000.0
saque = float(input("Informe o valor a sacar: R$ "))

# Estrutura
# variável = mensagem verdadeira if (condição) else mensagem falsa.
status = "Sucesso" if saldo >= saque else "Falha"
saldo -= saque

print(f"{status} ao realizar o saque de R$ {saque:.2f} reais, saldo atual R$ {saldo:.2f} reais.\n")