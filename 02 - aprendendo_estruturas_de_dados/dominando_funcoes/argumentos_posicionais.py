'''
    Argumentos antes da "/" são obrigatório o preenchinto de forma posicional e sem o identificador
'''


def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro(
    "Palio",
    1999,
    "ABC1234",
    marca="Fiat",
    motor="1.0 Firefly",
    combustivel="Gasolina"
)
