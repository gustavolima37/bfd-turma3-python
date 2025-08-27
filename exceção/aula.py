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


'''
Funções Built-in
- abs() # retorna o valor absoluto de um número
abs(-9)

- max() # retorna o valor máximo de uma sequência
max(8,7,14, 19) # retorna o valor máximo

- min() # retorna o valor minímo
min(2,3,4,5,6,7)

pow()
pow(base, exp) ou pow(base, exp, mod)

Retorna a potência de um número. É equivalente a usar o operador **. O terceiro argumento (mod) é opcional e, se fornecido, retorna o resto da divisão do resultado da potência por esse número.

pow(2, 3)

Retorna: 8 (que é 2 
3
 )

help()
help(objeto)

Exibe a documentação de um objeto, função, módulo ou palavra-chave do Python. É uma ferramenta fundamental para aprender sobre a linguagem diretamente no terminal.

help(print)

Retorna: A documentação completa sobre a função print().

range()
range(parada) ou range(inicio, parada, passo)

Cria uma sequência de números. É muito usado em loops for. A sequência gerada é um objeto range que economiza memória, pois só gera os números conforme necessário.

list(range(5))

Retorna: [0, 1, 2, 3, 4] (ele para antes de chegar no número 5)

round()
round(numero, ndigits)

Arredonda um número para o inteiro mais próximo ou para um número específico de casas decimais. Se o segundo argumento (ndigits) for omitido, ele arredonda para o inteiro.

round(4.789, 2)

Retorna: 4.79
'''