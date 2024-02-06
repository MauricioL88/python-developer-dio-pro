# Criando um dicionario anhinhado, simulando um banco de dados de uma agenda;

agenda = {
    "mauricio@email.com": {"nome": "Mauricio", "telefone": "99999-9991"},
    "evelin@email.com": {"nome": "Evelin", "telefone": "99999-9992"},
    "lucas@email.com": {"nome": "Lucas", "telefone": "99999-9993"},
    "beto@email.com": {"nome": "Beto", "telefone": "99999-9994"},
    "pablo@email.com": {"nome": "Pablo", "telefone": "99999-9995"}
}

# para exibir um dado do dicionário é necessário passar a chave;
print(agenda["evelin@email.com"]["telefone"])
print("\n")

# Interando um dicionário;
for chave in agenda:
    print(chave)

print("\n")
for chave, valor in agenda.items():
    print(chave, valor)
