class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    def __str__(self):
        return f'Produto: {self.nome} custa R$ {self.preco:.2f}'

    def desconto(self, valor):
        desc = self.preco - valor
        return desc

livro = Produto('Python Basico', 250.00)
desconto = livro.desconto(25)
print(f'O livro: {livro.nome}, custa R$ {livro.preco:.2f}, com descono fica: R$ {desconto:.2f}')
