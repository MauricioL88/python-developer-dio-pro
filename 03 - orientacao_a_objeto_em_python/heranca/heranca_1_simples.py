class Veiculo:
    # Atributos em comum
    def __init__(self, cor, placa, num_rodas):
        self.cor = cor
        self.placa = placa
        self.num_rodas = num_rodas

    # Comportamentos em comum
    def ligar_motor(self):
        print("Ligando motor...")

    # Método "__str__" exibe os dados do objeto
    def __str__(self):
        return f"{self.__class__.__name__} - {' | '.join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}"


class Motocicleta(Veiculo):
    pass


class Carro(Veiculo):
    pass


class Caminhao(Veiculo):
    # Sobrescrevendo o método contrutor "pai", personalizando para a classe "filha"
    def __init__(self, cor, placa, num_rodas, carregado):
        super().__init__(cor, placa, num_rodas)
        self.carregado = carregado

    # Comportamento específico de uma classe filha
    def esta_carregado(self):
        print(f"{"Sim, eu" if self.carregado else "Nao"} estou carregado...")


moto = Motocicleta("Verde", "AAA0000", 2)
moto.ligar_motor()

carro = Carro("Preto", "AAA0001", 4)
carro.ligar_motor()

caminhao = Caminhao("Azul", "AAA0002", 8, False)
caminhao.ligar_motor()

print(caminhao)
caminhao.esta_carregado()
