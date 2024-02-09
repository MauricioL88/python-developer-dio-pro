""" Ordenando os dicionários por chaves """

# Obter uma lista com as chaves do dicionário
dicionario = {
    'nome': 'Joao',
    'idade': 23,
    'cidade': 'Sao Paulo'
}

chaves = dicionario.keys()
print(chaves)

# Ordenar um dicionário pela chave
print("\nOrdem crescente:")
chaves_ordenadas = sorted(dicionario.keys())
for chave in chaves_ordenadas:
    print(chave, dicionario[chave])

# Ordenar um dicionário pela chave em ordem decrescente
print("\nOrdem decrescente:")
chaves_ordenadas = sorted(dicionario.keys(), reverse=True)
for chave in chaves_ordenadas:
    print(chave, dicionario[chave])
