class Animal:
    def __init__(self, num_patas):
        self.num_patas = num_patas
    
    # Método "__str__" exibe os dados do objeto
    def __str__(self):
        return f"{self.__class__.__name__} - {' | '.join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}"

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        super().__init__(**kw)
        self.cor_pelo = cor_pelo

class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class Leao(Mamifero):
    pass

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        super().__init__(**kw)
        self.cor_bico = cor_bico

class Ornitorrinco(Mamifero, Ave): # Sintaxe da herança multipla -> classe extendendo de outras 2 classes
    pass


gato = Gato('Preto', num_patas=4)
print(gato)

ornito = Ornitorrinco('Marrom', cor_bico='Amarelo', num_patas=2)
print(ornito)