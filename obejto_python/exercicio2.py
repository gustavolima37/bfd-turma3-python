'''
Exercício 2
Crie a classe Professor herdando de Pessoa.
- Atributos adicionais: disciplina, salario.
- Método: apresentar_professor() que exibe nome, idade e disciplina.

'''

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina, salario):
        super().__init__(nome, idade)
        self.disciplina = disciplina
        self.salario = salario
        
    def apresentar_professor(self):
        return (f'Olá! Meu nome é {self.nome}, tenho {self.idade} anos '
                f'e Leciono a disciplina de {self.disciplina}.')
    
professor1 = Professor('Andre', 52, 'Programação',5000)
    
print(professor1.apresentar_professor())