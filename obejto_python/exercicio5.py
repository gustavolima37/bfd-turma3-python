'''
Exercício 5
Utilize polimorfismo criando um método apresentar() em Professor e Estudante que funciona de
forma diferente em cada classe.
'''

# Reutilizando a classe Pessoa
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Método genérico de apresentação
    def apresentar(self):
        return f"Nome:  {self.nome}\nIdade: {self.idade} anos."

# Reutilizando a classe Professor
class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self.disciplina = disciplina

    # Método 'apresentar' com comportamento específico para Professor
    def apresentar(self):
        return super().apresentar() + f" \nLeciono a disciplina: {self.disciplina}."

# Criando a classe Estudante
class Estudante(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso

    # Método 'apresentar' com comportamento específico para Estudante
    def apresentar(self):
        return f"Nome:  {self.nome}\nIdade: {self.idade} anos\nEstudante de: {self.curso}."

pessoa1 = Pessoa("Ana", 40)
professor1 = Professor("Carlos", 50, "Física")
estudante1 = Estudante("Mariana", 22, "Engenharia de Software")

# Iterando sobre a lista e chamando o mesmo método
objetos_apresentar = [pessoa1, professor1, estudante1]

for objeto in objetos_apresentar:
    print(objeto.apresentar())