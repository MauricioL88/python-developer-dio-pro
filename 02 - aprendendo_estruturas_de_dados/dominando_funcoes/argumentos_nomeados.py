'''
    Argumentos após o "*" são obrigatório o preenchinto com o identificador
'''


def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro(
    modelo="Palio",
    ano=1999,
    placa="ABC1234",
    marca="Fiat",
    motor="1.0 Firefly",
    combustivel="Gasolina"
)