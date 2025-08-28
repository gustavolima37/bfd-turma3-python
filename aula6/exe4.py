import conversao 

'''
4. Importando Funções Específicas
○ Crie um módulo conversao.py com funções:
■ celsius_para_fahrenheit(c)
■ fahrenheit_para_celsius(f)
○ No programa principal, importe apenas a função
celsius_para_fahrenheit e use-a para converter um valor digitado pelo
usuário.
C = 5/9 x (F - 32)
'''

celcius = float(input('Digite a temperatura em ºC: '))
print(f'Convertendo para Fahrenheit: {celcius:.1f}º Celcius é igual a {conversao.celsius_para_fahrenheit(celcius)}º F')

fahrenheit = float(input('Digite a temperatura em ªF: '))
print(f'Convertendo para Celcius: {fahrenheit:.1f}º Fahrenheit é igual a {conversao.fahrenheit_para_celsius(fahrenheit)}º C')