'''
Exercício 16: Contar palavras em uma frase (função de string) Peça uma frase e
mostre quantas palavras ela possui.
'''
frase = input('Digite uma frase: ').strip().lower() #strip() retirando espaços antes e depois da frase, lower() tudo minusculo
palavra = frase.split() #split() separando a frase por palavras e criando uma lista
print(palavra)
quantidade = len(palavra) #len() contando cada palavra na lista 
print(f'A frase - {frase} - tem: {quantidade} palavras.')