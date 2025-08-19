#nome_cliente = input('Digite seu nome: ')
#print('Nome do cliente: ', nome_cliente)

#nome_cliente = input('Digite seu nome: ')
#print(f'Nome do cliente: {nome_cliente}')

print("---- Cadastro Online de Clientes ----")
nome_cliente = input('Digite seu nome: ')
print(f'Olá, {nome_cliente} Seja bem-vindo!')

idade = int(input('Digite sua idade: '))
print(f'Daqui há 10 anos você terá: {idade + 10} anos')

produto = float(input('Digite o valor de um produto aleatorio: '))
desconto = produto * 0.10
print(f'Este produto tem desconto de 10%, seu novo preço é {produto - desconto:.2f}')

matricula = input('Você esta matriculado? (Sim/Não) ').strip().lower()
matriculado = matricula == 'sim'
print(f'Sua resposta foi: {matriculado}')

    