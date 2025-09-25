class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def __str__(self):
        return f'Nome: {self.nome}\nIdade: {self.idade}'

pessoa1 = Pessoa('Gustavo', 38)
print(pessoa1)