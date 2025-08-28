import tabuada as tb
'''
3. Importação com Alias
○ Crie um módulo tabuada.py que tenha uma função mostrar_tabuada(n)
que imprime a tabuada de um número.
○ No programa principal, importe o módulo usando um apelido (import
tabuada as tb) e mostre a tabuada do número 7.
'''

numero = int(input('Digite um numero para ver sua tabuada: '))
print('=' * 30)
print(f'A tabuada do numero {numero} é:')
tb.mostrar_tabuada(numero)
print('=' * 30)