menu = """
######## SISTEMA BANCÁRIO ########

1 - Depositar
2 - Sacar
3 - Extrato
0 - Sair

Escolha a operação:
"""

saldo = 0.00
VLR_MAX_SAQUE = 500.00
QTD_SAQUE = 3
numero_saque = 0
extrato = ""

while True:
    opcao = int(input(menu))    
    if opcao == 1:
        print("DEPOSITO:")
        valor = float(input("Qual valor deseja depositar: R$ "))
        if valor > 0.00:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f} reais.\n"
        else:
            print("Valor não permitido!\n")    
    elif opcao == 2:               
        if numero_saque < QTD_SAQUE:
            print("SAQUE:")
            valor = float(input("Qual valor deseja sacar: R$ "))
            if (valor > 0) and (valor <= VLR_MAX_SAQUE) and (saldo >= valor):
                saldo -= valor
                numero_saque += 1
                extrato += f"Saque: R$ {valor:.2f} reais.\n"
                print("Saque realizado!\n")
            else:
                print("Valor não permitido ou sem saldo!\n")
        else:
            print("Limite diário excedido!\n")
    elif opcao == 3:
        print("\n********** EXTRATO **********")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}.")
        print("*******************************")   
    elif opcao == 0:
        break    
    else:
        print("Opção inválida, favor digitar o valor correto!\n")
