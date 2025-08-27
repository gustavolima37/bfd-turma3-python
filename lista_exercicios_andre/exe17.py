'''
Exercício 17: Palíndromo (string invertida) Crie uma função que verifique se uma
palavra é um palíndromo.
'''
# Recebendo a frase
frase = input('Digite uma frase: ').strip().upper() #tirando espaços antes e apos, colocando tudo para maiusculo
# Colocando a frase em uma lista
palavra = frase.split() #criando uma lista com as palavras da frase
#juntando a lista em uma palavra só
junto = ''.join(palavra)
#criando o inverso da palavra usando fatiamento de string
inverso = junto[::-1]

'''
- Usando a função reversed() com join()

texto = "Recife"
invertido = ''.join(reversed(texto))
print(invertido)  # saída: "eficeR"
--------------------------------------------------------
- Usando o for pra percorrer a string e retornar o inverso

inverso = ''
for letra in range(len(junto) -1, -1, -1):
  inverso += junto[letra]
'''
print(f'O inverso de {junto} é {inverso}')
#verificando
if inverso == junto:
  print('Temos um palidromo.')
else:
  print('A frase digitada não é um palidromo.')