def exibir_mensagem():
    print("Olá mundo!")


# Função com parâmetro
# Declaração obrigatória de dados
def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")


# Função com parâmetro "default"
# Declaração não obrigatória de dados
def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")


exibir_mensagem()
exibir_mensagem_2(nome="Guilherme")
exibir_mensagem_3()
exibir_mensagem_3(nome="Chapie")
