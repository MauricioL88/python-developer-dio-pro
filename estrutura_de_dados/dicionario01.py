contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3333-2222"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3333-2223"},
    "melanie@gmail.com": {"nome": "Melanie", "telefone": "3333-2224"},
}

# Exibindo chave e valor do dicionário
for chave in contatos:
    print(chave, contatos[chave])

print("=" * 100)

# Outra forma de exibição
for chave, valor in contatos.items():
    print(chave, valor)
