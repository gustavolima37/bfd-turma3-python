from constantes import PI

'''
6. Módulo com Constantes
○ Crie um módulo constantes.py que contenha uma constante PI =
3.14159.
○ No programa principal, importe essa constante e calcule a área de um
círculo (raio fornecido pelo usuário).
'''

raio = float(input('Digite o raio do circulo: '))
area = PI * (raio ** 2)
print(f'A area do circulo com raio de {raio} é {area:.2f}')