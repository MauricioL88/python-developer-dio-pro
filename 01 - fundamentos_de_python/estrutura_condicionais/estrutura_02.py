import sys

opcao = int(input("Informe uma opção:\n[1] Sacar | [2] Extrato: "))

if opcao == 1:
    valor = float(input("Informe a quantia para o saque: R$ "))
    print(f"Valor de R$ {valor:.2f} sacado!\n")
elif opcao == 2:
    print("Exibindo o extrato...\n")
else:
    sys.exit("Opção Inválida!\n")
