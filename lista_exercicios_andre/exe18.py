'''
Exercício 18: Substituir palavras em frase Peça uma frase e substitua uma palavra
específica por outra
'''
frase = input('Digite uma frase: ')
print(frase)
palavra_antiga = input('Digite uma palavra que será trocada: ')
palavra_nova = input('Digite a nova palavra: ')
frase_modificada = frase.replace(palavra_antiga, palavra_nova) #usando tratamento de string com replace()
print(frase_modificada)
