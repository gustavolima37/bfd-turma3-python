'''
Exercício 7: Verificação de vogais (função de string) Peça uma letra e verifique se é
uma vogal usando funções de string.
'''
vogais = 'aeiouAEIOU'
letra = input('Digite uma letra pra saber se é vogal ou nao: ')
def verificador_vogais(letra):
  if  letra in vogais:
    print(f'Esta letra - {letra} - é uma vogal')
  else:
    print(f'Esta letra - {letra} - não é vogal.')
verificador_vogais(letra)