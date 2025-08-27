'''
Exercício 15: Função para calcular fatorial Crie uma função que calcule o fatorial de
um número.
'''

numero = int(input('Digite um numero: '))
fatorial = 1
if numero < 0:
  print('Não é possivel calcular numero negativo.')
elif numero == 0:
  print('Fatorial de 0 é 1')
else:
  for i in range(1, numero +1):
    fatorial *= i
  print(f'Fatorial de {numero} é {fatorial}')