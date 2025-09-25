class Disciplina:
    def __init__(self, nome_disciplina):
        self.nome_disciplina = nome_disciplina
        
    def __str__(self):
        return f'{self.nome_disciplina}'

class Professor:
    def __init__(self, prof_nome):
        self.prof_nome = prof_nome
        self.disciplinas = []

    def adicionar_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)
        
    def __str__(self):
        num_disciplinas = len(self.disciplinas)
        return f'Professor(a) {self.prof_nome} (Ministra {num_disciplinas} disciplina(s))'

class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.matriculas = []
        
    def matricular(self, disciplina):
        self.matriculas.append(disciplina)
        
    def __str__(self):
        num_matriculas = len(self.matriculas)
        return f'Aluno(a) {self.nome} (Matriculado em {num_matriculas} disciplina(s))'


#Criando objetos
professor1 = Professor('Julios')
materia1 = Disciplina('Português')
materia2 = Disciplina('Matemática')
aluno1 = Aluno('Gustavo')
aluno2 = Aluno('André')

#Criando os relacionamentos
professor1.adicionar_disciplina(materia1)
professor1.adicionar_disciplina(materia2)

aluno1.matricular(materia1)
aluno2.matricular(materia2)

#Apresentação
print(professor1)
print(aluno1)
print(aluno2)
print(f'Disciplina ministrada por {professor1.prof_nome}: {professor1.disciplinas[0]} e {professor1.disciplinas[1]}')
print(f'Disciplina de {aluno1.nome}: {aluno1.matriculas[0]}')