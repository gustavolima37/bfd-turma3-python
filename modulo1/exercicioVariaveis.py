
# 1.Conversão de Tipos
 
 
numero = '123'
print(f'String: {numero}', type(numero))
numero = int(numero)
print(f'INT: {numero}', type(numero))
numero = float(numero)
print(f'Float: {numero}', type(numero))

# 2. Operações com Sring

frase = 'Python é incrível!'
print(f'Quantidade de caracteres: {len(frase)}')
print(f'String toda em maiúscula: {(frase).upper()}')
nova_frase = frase.replace('incrível', 'poderoso')
print(f'Nova frase: {nova_frase}')

# 3. Listas e Indexação

numeros = [10,20,30,40,50]
print(f'Terceiro elemento: {numeros[2]}')
numeros.append(60)
print(numeros)
numeros.remove(20)
print(numeros)

# 4. Dicionários
aluno = {
    'nome': 'Maria',
    'idade': 22,
    'curso': 'Engenharia'
}

aluno['notas'] = [8.5,7.0,9.2]
print(aluno)
print(aluno['curso'])

# 5. Tuplas e Conjuntos

cores = ('vermelho', 'verde', 'azul', 'verde')
print(cores)
novas_cores = tuple(set(cores)) #removendo valores duplicados.
print(novas_cores)
novas_cores = novas_cores + ('amarelo',)
print(novas_cores)

# 6. Operações Matemáticas
a = 15 # int
b = 4 # int

divisao = a // b # divisão inteira = //
print(divisao)
resto = a % b  # resto da divisao %
print(resto)

# 7. Verificação de Tipos

lista = [42,3.14,'Python', True, [1,2]]
for elemento in lista:
    print(f'Elemento: {elemento} -> Tipo: {type(elemento).__name__}') # no final do type().__name__ muda de (<class> int) para apenas int.
    
# 8. Manipulação de Strings

palavra = 'programação'
palavra_invertida = palavra[::-1]
print(palavra_invertida)
if palavra == palavra_invertida:
    print(True)
else:
    print(False)

# 9. Listas Aninhadas

lista_matriz = [[1,2,3], [4,5,6], [7,8,9]]
print(lista_matriz[1][1])
lista_matriz[2][1] = 10
print(lista_matriz)

# 10.Desafio Final

estoque = {
    'maçã': 10,
    'banana': 5,
    'laranja': 8
}
print(estoque)
estoque['pera'] = 12
print(estoque)
del estoque['banana']
print(estoque)
for item in estoque:
    print(item)
print(list(estoque.keys()))