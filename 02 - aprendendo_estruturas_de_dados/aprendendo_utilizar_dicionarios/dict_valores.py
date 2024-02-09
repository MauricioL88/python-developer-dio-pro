""" Incluindo valor em um dicionário """

# Criando um dicionário vazio e adiciona o um par chave-valor
meu_dicionario = {}
meu_dicionario["chave"] = "valor"
print(meu_dicionario)

# Adicionando vários pares chave-valor ao mesmo tempo, utilizando o método "update()"
meu_dicionario.update(
    {"chave2": "valor2", "chave3": "valor3", "chave4": "valor4"})
print(meu_dicionario)

# Adcionando pares chave-valor atrevés de um loop
meu_dicionario2 = {}
for i in range(5):
    meu_dicionario2[i] = i**2

print(meu_dicionario2)
