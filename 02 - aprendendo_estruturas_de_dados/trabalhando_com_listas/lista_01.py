# Lista são objetos mutáveis, é possível alterar os seus valores após a sua criação;
# Suportam sequências negativas

# Como declarar listas:
# Declarando com dados
frutas = ["laranja", "maca", "uva"]

# Ou declarar vazia
frutas = []

# Interando caracteres com método construtor da classe
letras = list("python")

# Usando a função range
numeros = list(range(10))

# Declarando variados tipos de dados
carro = ["Ferrari", "F8", 420000, 2024, 2900, "ECB", True]

# Fatiamento
nomeLista = ["p", "y", "t", "h", "o", "n"]

print(nomeLista[2:]) # parâmetro aonde inicia a exibição da lista;
print(nomeLista[:2]) # parâmetro que indica a exibição do fim da lista;
print(nomeLista[1:3]) # delimitando a exibição do inicio e fim;
print(nomeLista[0:3:2]) # delimitando a exibição do inicio e fim com steps;
print(nomeLista[::]) # sem limitações;
print(nomeLista[::-1]) # inverte a ordem de exibição;

# Conhecer a posição interavel da lista
print("\n")
carros = ["gol", "celta", "palio"]

for indice, carro in enumerate(carros):
    print(f"{indice} : {carro}")
