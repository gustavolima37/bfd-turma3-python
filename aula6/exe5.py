import random as rd
'''
5. Usando Módulos Internos do Python
○ Importe o módulo random e faça um programa que sorteia um número
entre 1 e 10.
○ Peça para o usuário adivinhar o número sorteado.

'''
cont = 1
contV = contD = 0

while cont <= 3:
    numeros = rd.randint(1,10)
    print('Adivinhe o numero que o PC digitou e ganhe dele')
    usuario = int(input('Digite seu numero de 1 a 10: '))
    print(f'Você escolheu: {usuario} -- e o PC: {numeros} --')
    if usuario == numeros:
        print('Parabéns, Você acertou!!')
        contV +=1
    else:
        print('Não foi dessa vez...')
        contD +=1
    cont +=1
print('Acabou suas tentativas...Fim de jogo')
print(f'- Você: {contV}\n- PC: {contD}')