def somar(a, b):
    return a + b


# Passando uma função como referencia (não é necessário as parênteses)
def exibir_resultado(a, b, funcao):
    # Executando a função "anônima"
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")


exibir_resultado(10, 30, somar)
print()

# Variável como função
op = somar
print(op(25, 25))
