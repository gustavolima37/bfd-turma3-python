'''
Exercício 1
Crie a classe Pessoa com os atributos nome e idade. Instancie duas pessoas diferentes e exiba
seus dados.
'''

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
pessoa1 = Pessoa('Gustavo', 38)
pessoa2 = Pessoa('Deise', 32)

print('Dados da Pessoa 1:')
print(f'Nome: {pessoa1.nome}\nIdade: {pessoa1.idade}')
print('='* 20)
print('Dados da Pessoa 2:')
print(f'Nome: {pessoa2.nome}\nIdade: {pessoa2.idade}')