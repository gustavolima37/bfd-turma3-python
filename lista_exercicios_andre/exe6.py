'''
Exercício 6: Função soma de dois números Crie uma função que receba dois
números e retorne a soma deles.
'''
num1 = int(input('Digite um numero: '))
num2 = int(input('Digite um segundo numero: '))
def soma(a,b):
  return a + b
print(f'O numero {num1} + {num2} = {soma(num1,num2)}')