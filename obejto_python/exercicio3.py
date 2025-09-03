'''
Exercício 3
Crie a classe Estudante herdando de Pessoa.
- Atributos adicionais: curso, matricula.
- Método: apresentar_estudante() que exibe nome, idade e curso.
'''

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Estudante(Pessoa):
    def __init__(self, nome, idade, curso, matricula):
        super().__init__(nome, idade)
        self.curso = curso
        self.matricula = matricula
        
    def apresentar_estudante(self):
        return f'- Nome:  {self.nome}\n- Idade: {self.idade} anos\n- Curso: {self.curso}'
               
        
aluno1 = Estudante('João', 18, 'Português', 2025)
aluno2 = Estudante('Rafael', 25, 'Jornalismo', 2024)

print('Dados do Aluno 1:')
print(aluno1.apresentar_estudante())
# print(f'Nome: {Aluno1.nome}')
# print(f'Idade: {Aluno1.idade}')
# print(f'Curso: {Aluno1.curso}')
# print('='* 20)
# print('Dados do Aluno 2:')
# print(f'Nome: {Aluno2.nome}')
# print(f'Idade: {Aluno2.idade}')
# print(f'Curso: {Aluno2.curso}')