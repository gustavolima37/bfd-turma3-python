'''
Exceção
Try e Except em Python
O bloco try serve para testar um trecho de código que pode gerar erro.
O bloco except serve para tratar o erro sem que o programa quebre.
'''

# Exemplo
try:
    numero = int(input("Digite um número inteiro: "))
    resultado = 10 / numero
    print("Resultado:", resultado)
except ValueError:
    print("Erro: você não digitou um número válido.")
except ZeroDivisionError:
    print("Erro: não é possível dividir por zero.")
