def calcula_media(n,m):
    return (n+m) / 2


# Entrada
nome_estudante = input('Digite seu nome: ')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

# Processamento
media = calcula_media(nota1,nota2)

# Saida

print(f'A media do estudante {nome_estudante} é {media}')
