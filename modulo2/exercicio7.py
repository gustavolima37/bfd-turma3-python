class Livro:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    def __str__(self):
        return f'Livro: {self.nome}\n-> Valor: {self.valor}'

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f'--> {livro.nome} adicionado a Biblioteca.')

    def listar_livros(self):
        if not self.livros:
            print('A biblioteca esta vazia')
            return

        print('\n------- Catálogo de Livros -------')
        for i, livro in enumerate(self.livros, 1):
            print(f'{i}. {livro}')
        print('------------------------------------')

biblioteca = Biblioteca()
livro1 = Livro('Medusa', 35.00)
livro2 = Livro('MegaMan2', 28.00)
livro3 = Livro('PowerRanger 2022', 15.50)

biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)

biblioteca.listar_livros()

    