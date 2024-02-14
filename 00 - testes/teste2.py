def listar_itens(**kwargs):
    lista = "| ".join([f"{chave}: {valor} " for chave, valor in kwargs.items()])
    print(lista)


listar_itens(nome1="Mauricio", nome2="Evelin")
