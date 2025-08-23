'''
Exercício 13: Números pares até 20 (while) Mostre todos os números pares de 2 até
20 usando while.
'''
contador = 1 # começando a variavel valendo 1
pares = [] #lista para receber os numeros pares
while contador <= 20: # enquanto o contador for menor igual a 20 faça:
  if contador % 2 == 0: # se o contador dividido por 2 e tem sobra 0:
    pares.append(contador) # adicione na lista pares, o valor do contador
  contador += 1 # acrescenta +1 pro contador continuar.
print(f'Lista de numeros pares {pares}') # mostra na tela a lista de numeros pares obtidos.