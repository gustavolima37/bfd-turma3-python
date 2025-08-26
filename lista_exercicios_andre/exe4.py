'''
Exercício 4: Tabuada com for Peça um número e mostre sua tabuada de 1 a 10
usando for. Exercício
'''
numero = int(input('Digite um numero para ver sua tabuada: '))
for i in range(1,11):
  print(f'{numero} x {i} = {numero*i}')