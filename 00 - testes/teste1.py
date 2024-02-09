conta = 0
banco_dados = {}
saldo = 0.0

resp = 'N'
resp.lower()
while resp != 's':
    conta = len(banco_dados)
    nome = input("Digite o seu nome: ")
    cpf = int(input("Digite o seu CPF: "))

    banco_dados.update({
        conta: {
            'nome': nome,
            'cpf': cpf,
            'saldo': saldo
        }
    })

    print("\nTamanho do Banco de Dados: ", len(banco_dados))
    resp = input("\nDeseja sair?\nS | N: ")
    resp.lower()
    print("\n")

for chave, valor in banco_dados.items():
    print(chave, valor)
print("\n")
