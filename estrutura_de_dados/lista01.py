listaNun = []
cont = 0
qtd = int(input("Quando números deseja cadastrar: "))

while cont < qtd:
    print("")
    num = int(input("Digite um número: "))
    listaNun.append(num)
    cont += 1
print("\n")
resultado = [numero for numero in listaNun if numero % 2 == 0]

for numPar in resultado:
    print(f"Número par: {numPar}")
