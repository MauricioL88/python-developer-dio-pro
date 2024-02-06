'''
***segundo desafio***

modularizando o algorítmo com funções

criar funções:
(reaproveitar os códigos existentes)
-depositar
	deve receber os argumentos apenas por posição;
	sugestão de argumentos:
		saldo, valor, extrato | retorno: saldo e extrato
-sacar
	deve receber os argumentos apenas por nome;
	sugestão de argumentos:
		saldo, valor, extrato, limite, num_saques, limite_saques | retorno: saldo e extrato
-visualizar_extrato
	deve recever os argumentos por posição e nome;
	posicionais:
		saldo
	nomeados:
		extrato
(novo)
-criar_usuario
    regra: 
        deverá criar uma lista com os atributos: nome, data de nascimento, cpf e endereço;
        endereço é uma string com o formato: logadouro, numero, bairro, cidade, sigla estado;
        cpf deve ser armazenado somente em numeros;
        não pode cadastrar dois usuário com o mesmo cpf;
-criar_conta_corrente
    regra:
        deverá criar uma lista com os atributos: agencia, numero da conta e usuario;
        numero da conta é sequencial, iniciando com 1;
        numero da agencia é fixo com o valor padão "0001";
        o usuario pode ter mais de uma conta, mas uma conta pertence a somente um usuário;
    dica:
        para vincular um usuario a uma conta, filtre a lista de usuarios buscando o numero do
        cpf informado para cada usuario da lista;
-podendo criar mais funções

'''
import textwrap

def menu():
    return """
    ######## SISTEMA BANCÁRIO ########

    1 - Depositar
    2 - Sacar
    3 - Extrato
    0 - Sair

    Escolha a operação:
    """

def depositar(saldo, valor, extrato, /):
        valor = float(input("Qual valor deseja depositar: R$ "))
        if valor > 0.00:
            saldo += valor
        else:
            print("Valor não permitido!\n")
    


saldo = 0.00
VLR_MAX_SAQUE = 500.00
QTD_SAQUE = 3
numero_saque = 0
extrato = ""

while True:
    opcao = int(input(menu()))
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
