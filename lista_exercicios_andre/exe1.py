'''
Exercício 1: Par ou ímpar (if/else) Peça um número ao usuário e verifique se é par
ou ímpar usando if/else.
'''
numero = int(input('Digite um numero para saber se é par ou ímpar: '))
verificar_par_impar = lambda numero: 'par' if numero % 2 == 0 else 'impar'
print(verificar_par_impar(numero))