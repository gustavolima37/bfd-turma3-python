class Animal:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return f'Animal: {self.nome}'

class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)
        self.raca = raca

    def __str__(self):
        return f'Cachorro: {self.nome} da raça {self.raca}'

    def falar(self):
        return ' -> Au Auuu'

class Gato(Animal):
    def __init__(self, nome, local):
        super().__init__(nome)
        self.local = local

    def __str__(self):
        return f'Gato: {self.nome} do(a) {self.local}'

    def falar(self):
        return f' -> Miau Miauu'

cachorrin = Cachorro('Apolo', 'Buldog')
print(cachorrin, cachorrin.falar())

gatin = Gato('Muzan', 'Apartamento')
print(gatin, gatin.falar())