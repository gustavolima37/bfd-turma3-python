import matematica
'''
2. Módulo de Operações Matemáticas
○ Crie um módulo chamado matematica.py com funções:
■ soma(a, b)
■ subtracao(a, b)
○ No programa principal, importe o módulo e peça ao usuário dois
números para calcular a soma e a subtração.
'''

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite o segundo numero: '))

print(f'Soma: {num1} + {num2} = {matematica.soma(num1,num2)}')