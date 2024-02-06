'''
    args(*) = adiciona uma tupla
    kwargs(**) = adiciona um dicionário
'''

def exibir_poema(data_extensao, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join(
        [f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extensao}\n\n{texto}\n\n{meta_dados}\n"
    print(mensagem)


exibir_poema(
    "Dom, 04 de Fevereiro de 2024",
    "Zen of Python",
    "Beatiful is better than ugly.",
    "...",
    autor="Tim Peters", ano=1999)

def nome_sobrenome(titulo, **kwargs):
    agenda = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    msg = f"{titulo}\n{agenda}\n"
    print(msg)

nome_sobrenome("Lista de Chamada:", nome1="Mauricio", nome2="Evelin", nome3="Mary", nome4="Edna")
