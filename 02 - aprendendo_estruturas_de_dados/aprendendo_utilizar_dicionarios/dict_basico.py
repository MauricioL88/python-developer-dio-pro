""" Sintáxe básica de um dicionário """

# Acessando um valor pelo nome da chave
dicionario = {'nome': 'João', 'idade': 25, 'cidade': 'Sao Paulo'}
print(dicionario['idade'])

# Acessar um valor utilizando a função "get()"
print(dicionario.get('idade'))

# Alterando um valor no dicionário
dicionario['idade'] = 30
print(dicionario)

# Adicionando um valor no dicionário
dicionario['profissao'] = 'Programador'
print(dicionario)

# Obter uma lista com as chaves do dicionário
print(dicionario.keys())

# ou...
for chave in dicionario:
    print(chave)

# Obter uma lista com os valores do dicionário
print(dicionario.values())

# ou...
for valor in dicionario.values():
    print(valor)
