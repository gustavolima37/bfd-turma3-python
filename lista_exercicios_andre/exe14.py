'''
Exercício 14: Função para verificar número primo Crie uma função que receba um
número e retorne se ele é primo.
'''
def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Exemplo de uso
numero = int(input("Digite um número: "))
if eh_primo(numero):
    print(f"{numero} é primo!")
else:
    print(f"{numero} não é primo.")