# Compreensão de listas

# Filtro versão 1
numeros = [1, 30, 20, 40, 55, 100, 12]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

# Filtro versão 2
outrosNumeros = [1, 30, 20, 40, 55, 100, 12]
# Estrutura: retorno, laço for para interar e a condição
outrosPares = [numero for numero in outrosNumeros if numero % 2 == 0]

# Modificando valores versão 1
listaNumeros = [1, 30, 20, 40, 55, 100, 12]
quadrado = []

for lista in listaNumeros:
    quadrado.append(lista ** 2)
    print(quadrado, end=" ")

# Modificando valores versão 2
listaNumeros2 = [1, 30, 20, 40, 55, 100, 12]
quadrado = [lista2 ** 2 for lista2 in listaNumeros2]
