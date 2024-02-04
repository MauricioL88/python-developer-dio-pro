def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso! {marca} / {modelo} / {ano} / {placa}")


# Somente com a declaração do dado
salvar_carro("Volkswagen", "Polo", 2022, "ABC1111")
# Função com declaração com os argumentos padrões
salvar_carro(marca="Chevrolet", modelo="Onix", ano=2020, placa="ABC1112")
# Função com delcaração de argumentos nomeados
salvar_carro(ano=2023, marca="Fiat", placa="ABC1113", modelo="Argo")
# Como declarar os dados de um dicionário nos argumentos de uma função (ou kwargs)
salvar_carro(**{"marca": "Ford", "modelo": "Focus", "ano": 2018, "placa": "ABC1114"})
