'''
Exercício 4
Implemente encapsulamento para o salário do professor, permitindo apenas alteração através de
um método ajustar_salario(valor).

'''

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina, salario):
        super().__init__(nome, idade)
        self.disciplina = disciplina
        self.__salario = salario #encapsulamento do salario
        
    def apresentar_professor(self):
        return (f'Olá! Meu nome é {self.nome}, tenho {self.idade} anos '
                f'e Leciono a disciplina de {self.disciplina}.')
    
    def get_salario(self):
        return self.__salario
    
    def ajustar_salario(self, novo_salario):
        if novo_salario > 0:
            self.__salario = novo_salario
            print(f'Salário ajustado com sucesso para R$ {self.__salario}.')
        else:
            print('Erro: O novo salário deve ser um valor positivo.')
    
    
    
    
professor1 = Professor('Andre', 52, 'Programação',5000)
print(professor1.apresentar_professor())
#print(professor1.__salario) # vai dar erro.
print(f'Salário atual: R$ {professor1.get_salario()}')
professor1.ajustar_salario(6000)
print(f'Novo salário: R$ {professor1.get_salario()}')
