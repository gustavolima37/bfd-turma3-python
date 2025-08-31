import os
import platform
# Dicionário global para armazenar os funcionários
funcionarios = {}

#Funções

# Calcular o INSS
def calcular_inss(salario_bruto):
    # Tabela de contribuição do INSS (valores de 2024)
    # Lista de tuplas: (limite da faixa, alíquota)
    tabela_inss = [
        (1518.00, 0.075),
        (2793.88, 0.09),
        (4190.83, 0.12),
        (8157.41, 0.14)
    ]

    valor_inss = 0
    salario_base = salario_bruto

    # Itera sobre as faixas para calcular a contribuição
    for limite, aliquota in tabela_inss:
        # Se o salário base for maior que o limite da faixa
        if salario_base > limite:
            # Calcula o valor do desconto sobre o limite da faixa
            valor_inss += limite * aliquota
            # Diminui o salário base para a próxima faixa
            salario_base -= limite
        else:
            # Se o salário base for menor ou igual ao limite,
            # calcula o desconto sobre o valor restante e sai do loop
            valor_inss += salario_base * aliquota
            break
            
    return valor_inss

# Função principal para calcular o salário
def calcular_salario():
    print('\n+++++ Cálculo Deste Funcionário +++++')

    todos_funcionarios()
    nome = input('Digite o nome do funcionário: ').strip().upper()
    
    # Assume que o dicionário `funcionarios` existe globalmente
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
    sindicato_percentual = funcionarios[nome]['sindicato']
    salario_bruto = valor_hora * horas
    
    # Chamada correta da função calcular_inss, passando o salário bruto
    inss = calcular_inss(salario_bruto)

    # Lógica simplificada para o Imposto de Renda
    if salario_bruto <= 2259.20:
        percentual_ir = 0.0
    elif salario_bruto <= 2826.65:
        percentual_ir = 7.5
    elif salario_bruto <= 3751.05:
        percentual_ir = 15.0
    elif salario_bruto <= 4664.68:
        percentual_ir = 22.5
    else:
        percentual_ir = 27.5
        
    imposto_renda = salario_bruto * (percentual_ir / 100)
    
    sindicato = salario_bruto * sindicato_percentual
    salario_liquido = salario_bruto - (imposto_renda + inss + sindicato)

    print('=' * 50)
    print(f'\nResumo para o funcionário: {nome}')
    print(f'Salário bruto: R$ {salario_bruto:.2f}')
    print(f'INSS: R$ {inss:.2f}')
    print(f'Sindicato ({sindicato_percentual*100:.1f}%): R$ {sindicato:.2f}')
    
    if percentual_ir == 0:
        print(f'Imposto de Renda: Isento')
    else:
        print(f'Imposto de Renda ({percentual_ir:.1f}%): R$ {imposto_renda:.2f}')
        
    print(f'Salário líquido: R$ {salario_liquido:.2f}\n')  
    print('=' * 50)

# Cadastrar Funcionário
def cadastrar_funcionario():
    print('\n➕ Cadastro de Funcionário')

    # Loop para garantir que o nome não seja vazio e não exista
    while True:
        nome = input('Digite o nome do funcionário: ').strip().upper()
        cargo = input('Digite o cargo: ').strip().upper()
        cidade = input('Digite a cidade: ').strip().upper()
        if not nome:
            print('⚠️ O nome não pode estar vazio.')
        elif nome in funcionarios:
            print(f'⚠️ O funcionário "{nome}" já está cadastrado.')
            # Adiciona opção para tentar outro nome ou sair
            if input('Deseja tentar outro nome? (s/n) ').lower() != 's':
                return
        else:
            break

    # Loop para garantir que o valor da hora seja válido
    while True:
        try:
            valor_hora = float(input('Digite o valor da hora de trabalho: '))
            if valor_hora > 0:
                break
            else:
                print('⚠️ O valor deve ser maior que zero.')
        except ValueError:
            print('⚠️ Digite um número válido.')

    # Define o percentual do sindicato como um valor fixo
    sindicato_fixo = 0.05  # 5%

    # Adiciona o funcionário ao dicionário
    funcionarios[nome] = {
        'cargo': cargo,
        'cidade': cidade,
        'valor_hora': valor_hora,
        'sindicato': sindicato_fixo
    }

    print(f'\n✅ Funcionário cadastrado com sucesso!')
    print(f'Nome: {nome}')
    print(f'Cargo: {cargo}')
    print(f'Cidade: {cidade}')
    print(f'Valor da hora: R$ {valor_hora:.2f}\n')
    
# Alterar Fucionário
def alterar_funcionario():
    print('\n✏️ Alterar Funcionário')

    # Exibe a lista de funcionários para ajudar o usuário
    todos_funcionarios()
    nome_atual = input('Digite o nome do funcionário que deseja alterar: ').strip().upper()

    # Verifica se o funcionário existe usando a chave correta (o nome)
    if nome_atual not in funcionarios:
        print(f'❌ Funcionário "{nome_atual}" não encontrado.\n')
        return

    # Loop principal para permitir múltiplas alterações
    while True:
        dados_atuais = funcionarios[nome_atual]
        print(f'\n🔎 Dados atuais de {nome_atual}:')
        print(f"   Nome: {nome_atual}")
        print(f"   Cargo: {dados_atuais['cargo']}")
        print(f"   Cidade: {dados_atuais['cidade']}")
        print(f"   Valor da hora: R$ {dados_atuais['valor_hora']:.2f}")

        print('\nO que você deseja alterar?')
        print('1 - Nome')
        print('2 - Cargo')
        print('3 - Cidade')
        print('4 - Valor da hora')
        print('5 - Sair')

        opcao = input('Digite o número da opção desejada: ').strip()

        if opcao == '1':
            while True:
                novo_nome = input('Digite o novo nome do funcionário: ').strip().upper()
                if not novo_nome:
                    print('⚠️ O nome não pode estar vazio.')
                elif novo_nome in funcionarios:
                    print(f'⚠️ O nome "{novo_nome}" já está em uso. Tente outro.')
                else:
                    # Armazena os dados atuais antes de alterar a chave
                    dados_para_mover = funcionarios[nome_atual]
                    
                    # Exclui a chave antiga e cria uma nova com os mesmos dados
                    del funcionarios[nome_atual]
                    funcionarios[novo_nome] = dados_para_mover
                    
                    print(f'✅ Nome do funcionário "{nome_atual}" alterado para "{novo_nome}".\n')
                    # A variável que guarda o nome atual precisa ser atualizada
                    nome_atual = novo_nome
                    break

        elif opcao == '2':
            novo_cargo = input('Digite o novo cargo: ').strip().upper()
            if novo_cargo: # Verifica se a entrada não está vazia
                funcionarios[nome_atual]['cargo'] = novo_cargo
                print(f'✅ Cargo de {nome_atual} atualizado para "{novo_cargo}".\n')
            else:
                print('⚠️ O cargo não pode estar vazio.')

        elif opcao == '3':
            nova_cidade = input('Digite a nova cidade: ').strip().upper()
            if nova_cidade:
                funcionarios[nome_atual]['cidade'] = nova_cidade
                print(f'✅ Cidade de {nome_atual} atualizada para "{nova_cidade}".\n')
            else:
                print('⚠️ A cidade não pode estar vazia.')

        elif opcao == '4':
            while True:
                try:
                    novo_valor = float(input('Digite o novo valor da hora: '))
                    if novo_valor > 0:
                        funcionarios[nome_atual]['valor_hora'] = novo_valor
                        print(f'✅ Valor da hora de {nome_atual} atualizado para R$ {novo_valor:.2f}\n')
                        break
                    else:
                        print('⚠️ O valor deve ser maior que zero.')
                except ValueError:
                    print('⚠️ Digite um número válido.')

        elif opcao == '5':
            print('Saindo da alteração.')
            return

        else:
            print('Opção inválida. Por favor, digite um número válido.')

# Excluir funcionáriop
def excluir_funcionario():
    print('\n🗑️ Excluir Funcionário')

    todos_funcionarios()
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
    for nome, dados in funcionarios.items():
        print(f'Nome: {nome}')
        print(f"Cargo: {dados.get('cargo', 'Não informado')}")
        print(f"Cidade: {dados.get('cidade', 'Não informada')}")
        print(f"Valor da hora: R$ {dados['valor_hora']:.2f}")
        print('-' * 30)

# Função pra limpar tela depois de cada ação
def limpar_tela():
    """Limpa a tela do terminal, compatível com Windows, macOS e Linux."""
    sistema_operacional = platform.system()
    if sistema_operacional == 'Windows':
        os.system('cls')
    else:  # 'Linux' ou 'Darwin' (macOS)
        os.system('clear')

# Função de menu do sistema
def menu():
    limpar_tela() # Limpa a tela antes de exibir o menu
    print('=' * 50)
    print('\n+++++ Gerenciamento de Funcionários +++++')
    print('-' * 50)
    print('1 - Cadastrar Funcionário')
    print('2 - Alterar Funcionário')
    print('3 - Listar Funcionários')
    print('4 - Calcular Salário')
    print('5 - Excluir Funcionário')
    print('6 - Sair')
    print('=' * 50)

# O loop principal, com as chamadas de limpar_tela()
# Versão otimizada da função rodar_programa
def rodar_programa():
    while True:
        limpar_tela()
        menu()
        
        opcao = input('Digite a opção desejada: ').strip()
        
        if opcao == '1':
            cadastrar_funcionario()
        elif opcao == '2':
            alterar_funcionario()
        elif opcao == '3':
            todos_funcionarios()
        elif opcao == '4':
            calcular_salario()
        elif opcao == '5':
            excluir_funcionario()
        elif opcao == '6':
            print('=' * 50)
            print('---=== Encerrando o sistema ===---')
            print('=' * 50)
            break
        else:
            print('Opção inválida! Tente novamente.')

        # Espera o usuário pressionar Enter apenas se não for a opção 'Sair'
        if opcao != '6':
            input('\nPressione Enter para continuar...')
            
# Chamando a função pra iniciar o sistema
rodar_programa()