# Exe3
# Peça ao usuário para digitar 3 números inteiros e:
# Use a função max() para mostrar o maior número.
# Use a função min() para mostrar o menor número.
# Use a função sum() para mostrar a soma deles.

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite um segundo numero: '))
num3 = int(input('Digite um terceiro numero: '))

maior = max(num1, num2, num3)
menor = min(num1, num2, num3)
soma = [num1, num2, num3]

# A função sum(), so pode receber 2 argumentos, por isso criei uma lista
# assim ela soma todos os elementos dentro desta lista.

print(f'Os numeros digitados foram: {num1}, {num2}, {num3}')
print(f'O maior deles é {maior}')
print(f'O menor deles é {menor}')
print(f'A soma dos 3 numeros é {sum(soma)}')