'''
Exercício 10: Maior de três números (if/elif/else) Leia três números e mostre qual é o
maior.
'''
num1 = int(input('Digite um numero aleatorio: '))
num2 = int(input('Digite mais um numero: '))
num3 = int(input('Digite mais um numero: '))
if num1 >= num2 and num1 >= num3:
  print(f'O maior é {num1}')
elif num2 >= num1 and num2 >= num3:
  print(f'O maior é {num2}')
else:
  print(f'O maior é {num3}')