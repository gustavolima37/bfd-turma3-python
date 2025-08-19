# Dicionário global para armazenar os funcionários
funcionarios = {}

#Funções

# Calcular Salario do Funcionário
def calcular_salario():
    print('\n+++++ Cálculo Deste Funcionário +++++')

    nome = input('Digite o nome do funcionário: ').strip().upper()
    if nome not in funcionarios:
        print(f'Funcionário "{nome}" não encontrado.\n')
        return

    while True:
        try:
            horas = float(input('Digite a quantidade de horas trabalhadas: '))
            if horas >= 0:
                break
            else:
                print('As horas devem ser zero ou mais.')
        except ValueError:
            print('Digite um número válido.')

    valor_hora = funcionarios[nome]['valor_hora']
    inss_percentual = funcionarios[nome]['inss']
    sindicato_percentual = funcionarios[nome]['sindicato']
    salario_bruto = valor_hora * horas

    if salario_bruto <= 2259.20:
        imposto_renda = 0
        percentual_ir = 0
        mensagem_ir = 'Isento'
    elif salario_bruto <= 2826.65:
        percentual_ir = 7.5
        imposto_renda = salario_bruto * (percentual_ir / 100)
        mensagem_ir = ''
    elif salario_bruto <= 3751.05:
        percentual_ir = 15
        imposto_renda = salario_bruto * (percentual_ir / 100)
        mensagem_ir = ''
    elif salario_bruto <= 4664.68:
        percentual_ir = 22.5
        imposto_renda = salario_bruto * (percentual_ir / 100)
        mensagem_ir = ''
    else:
        percentual_ir = 27.5
        imposto_renda = salario_bruto * (percentual_ir / 100)
        mensagem_ir = ''

    inss = salario_bruto * inss_percentual
    sindicato = salario_bruto * sindicato_percentual
    salario_liquido = salario_bruto - (imposto_renda + inss + sindicato)

    print('=' * 50)
    print(f'\nResumo para o funcionário: {nome}')
    print(f'Salário bruto: R$ {salario_bruto:.2f}')
    print(f'INSS ({inss_percentual*100:.1f}%): R$ {inss:.2f}')
    print(f'Sindicato ({sindicato_percentual*100:.1f}%): R$ {sindicato:.2f}')
    if percentual_ir == 0:
        print(f'Imposto de Renda: {mensagem_ir}')
    else:
        print(f'Imposto de Renda ({percentual_ir:.1f}%): R$ {imposto_renda:.2f}')
    print(f'Salário líquido: R$ {salario_liquido:.2f}\n')
    print('=' * 50)

# Cadastrar Funcionário
def cadastrar_funcionario():
    print('Cadastro de Funcionário')

    # Loop para garantir que o nome não seja vazio
    while True:
        nome = input('Digite o nome do funcionário: ').strip().upper()
        if nome:
            break
        print('O nome não pode estar vazio.')

    # Loop para garantir que o valor da hora seja válido
    while True:
        try:
            valor_hora = float(input('Digite o valor da hora de trabalho: '))
            if valor_hora > 0:
                break
            else:
                print('O valor deve ser maior que zero.')
        except ValueError:
            print('Digite um número válido.')

    # Define percentuais fixos
    inss = 0.08         # 8%
    sindicato = 0.05    # 5%

    # Adiciona o funcionário ao dicionário
    funcionarios[nome] = {
        'valor_hora': valor_hora,
        'inss': inss,
        'sindicato': sindicato
    }

    print(f'Funcionário {nome} cadastrado com sucesso!\n')

# Alterar Fucionário
def alterar_funcionario():
    print('\n✏️ Alterar Funcionário')

    # Solicita o nome do funcionário a ser alterado
    nome = input('Digite o nome do funcionário que deseja alterar: ').strip().upper()

    # Verifica se o nome existe no dicionário
    if nome not in funcionarios:
        print(f'❌ Funcionário "{nome}" não encontrado.\n')
        return  # Sai da função se não encontrar

    # Exibe o valor atual
    valor_atual = funcionarios[nome]['valor_hora']
    print(f'🔎 Valor atual da hora: R$ {valor_atual:.2f}')

    # Solicita novo valor da hora com validação
    while True:
        try:
            novo_valor = float(input('Digite o novo valor da hora: '))
            if novo_valor > 0:
                break
            else:
                print('⚠️ O valor deve ser maior que zero.')
        except ValueError:
            print('⚠️ Digite um número válido.')

    # Atualiza o valor no dicionário
    funcionarios[nome]['valor_hora'] = novo_valor
    print(f'✅ Valor da hora de {nome} atualizado para R$ {novo_valor:.2f}\n')

# Excluir funcionáriop
def excluir_funcionario():
    print('\n🗑️ Excluir Funcionário')

    # Solicita o nome do funcionário
    nome = input('Digite o nome do funcionário que deseja excluir: ').strip().upper()

    # Verifica se o funcionário existe
    if nome not in funcionarios:
        print(f'❌ Funcionário "{nome}" não encontrado.\n')
        return

    # Confirma exclusão
    confirmacao = input(f'Tem certeza que deseja excluir {nome}? (S/N): ').strip().upper()
    if confirmacao == 'S':
        del funcionarios[nome]
        print(f'✅ Funcionário "{nome}" excluído com sucesso.\n')
    else:
        print('🚫 Exclusão cancelada.\n')

# Relação de todos os funcionários cadastrados no Sistema
def todos_funcionarios():
    print('\n📄 Lista de Funcionários Cadastrados')

    # Verifica se o dicionário está vazio
    if len(funcionarios) == 0:
        print('⚠️ Nenhum funcionário cadastrado ainda.\n')
        return  # Sai da função se não houver funcionários

    # Percorre o dicionário e exibe os dados de cada funcionário
    for nome in funcionarios:
        valor_hora = funcionarios[nome]['valor_hora']
        print(f'Nome: {nome}')
        print(f'Valor da hora: R$ {valor_hora:.2f}')
        print('-' * 30)


def menu():
    print('++++++++++ Sistema Folha de Pagamento ++++++++++')
    print('=' * 50)
    print('---------- Menu de Opções do Sistema ---------')

    print('1 - Cadastrar Funcionario')
    print('2 - Alterar Funcionario')
    print('3 - Todos Funcionarios')
    print('4 - Calcular Salario Funcionario')
    print('5 - Excluir Funcionario')
    print('6 - Encerrar o Sistema')
    print('-' * 50)
    
print('++++++++++ Sistema Folha de Pagamento ++++++++++')
print('=' * 50)
print('---------- Menu de Opções do Sistema ---------')

print('1 - Cadastrar Funcionario')
print('2 - Alterar Funcionario')
print('3 - Todos Funcionarios')
print('4 - Calcular Salario Funcionario')
print('5 - Excluir Funcionario')
print('6 - Encerrar o Sistema')

print('=' * 50)

#Entrada

while True:
    
    opcao = input('Digite a opção desejada: ')
    if opcao == '1':
        cadastrar_funcionario()
        menu()
    elif opcao == '2':
        alterar_funcionario()
        menu()
    elif opcao == '3':
        todos_funcionarios()
        menu()
    elif opcao == '4':
        calcular_salario()
        menu()
    elif opcao == '5':
        excluir_funcionario()
        menu()
    elif opcao == '6':
        print('Encerrando o sistema... Até logo!')
        break
    else:
        print('Opção Invalida!')