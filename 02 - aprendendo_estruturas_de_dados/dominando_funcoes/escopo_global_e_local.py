salario = 2000.0

def salario_bonus(valor):
    global salario
    salario += valor
    return salario

print(salario_bonus(500.0))
