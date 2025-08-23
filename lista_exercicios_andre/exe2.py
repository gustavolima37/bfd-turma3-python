'''
Exercício 2: Classificação de idade (if/elif/else) Peça a idade de uma pessoa e
classifique como Criança, Adolescente ou Adulto.
'''
idade = int(input('Digite sua idade: '))
verificador_idade = lambda idade: 'Uma criança' if idade <= 11 else ('Adolescente' if idade <= 17 else 'Adulto')
print(verificador_idade(idade))