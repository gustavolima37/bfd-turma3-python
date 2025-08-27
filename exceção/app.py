import matematica 
# Principal


print('---------- Calculadora BFD ----------')
print('=' * 30)
print('1. Somar')
print('2. Subtrair')
print('3. Dividir')
print('4. Multiplicar')
print('5. Sair')
print('=' * 30)

while True:
    
    opcao = input('Digite uma opção acima: ')
    if opcao == '5':
        print('Finalizando a Calculadora!')
        break
    if opcao not in ['1','2','3','4']:
        print('Opção Inválida!!')
        continue
    
   # Loop para garantir um número válido para numero1
    while True:
        try:
            numero1 = float(input('Digite o primeiro numero: '))
            break
        except ValueError:
            print('Entrada inválida! Digite apenas números.')
            
    # Loop para garantir um número válido para numero2
    while True:
        try:
            numero2 = float(input('Digite o segundo numero: '))
            break
        except ValueError:
            print('Entrada inválida! Digite apenas números.')
     
    if opcao == '1':
        print(f'Adição: {numero1} + {numero2} = {matematica.somar(numero1,numero2)}')
    elif opcao == '2':
        print(f'Subtração:  {numero1} - {numero2} = {matematica.subtrair(numero1, numero2)}')
    elif opcao == '3':
        print(f'Divisão: {numero1} / {numero2} = {matematica.dividir(numero1,numero2)}')
    elif opcao == '4':
        print(f'Multiplicação: {numero1} x {numero2} = {matematica.multiplicar(numero1,numero2)}')

    continuar = input('Deseja continuar na calculadora? (S/N) ').upper()
    if continuar != 'S':
        print('Encerrando... Até a próxima!')
        break

