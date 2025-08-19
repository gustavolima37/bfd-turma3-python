import os
import platform
# Dicionário global para armazenar os funcionários
funcionarios = {}

#Funções

#Com base no salario, classifica a função
def classificar_cargo(salario_bruto):
    if salario_bruto <= 800:
        return "Jovem Aprendiz"
    elif salario_bruto <= 1600:
        return "Funcionário Base"
    elif salario_bruto <= 2500:
        return "Auxiliar Base"
    elif salario_bruto <= 3500:
        return "Supervisor"
    elif salario_bruto <= 6000:
        return "Gerente"
    else:
        return "Gerente Geral"

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
    
    # Chama a função para classificar o cargo com base no salário bruto
    cargo = classificar_cargo(salario_bruto)
    
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
    print(f'Cargo: {cargo}')  # Nova linha para o cargo
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
        'valor_hora': valor_hora,
        'sindicato': sindicato_fixo
    }

    print(f'\n✅ Funcionário {nome} cadastrado com sucesso!')
    print(f'   Valor da hora: R$ {valor_hora:.2f}\n')
    
# Alterar Fucionário
def alterar_funcionario():
    print('\n✏️ Alterar Funcionário')

    # Exibe a lista de funcionários para ajudar o usuário
    todos_funcionarios()
    nome_atual = input('Digite o nome do funcionário que deseja alterar: ').strip().upper()

    if nome_atual not in funcionarios:
        print(f'❌ Funcionário "{nome_atual}" não encontrado.\n')
        return

    # Loop principal para permitir múltiplas alterações
    while True:
        dados_atuais = funcionarios[nome_atual]
        print(f'\n🔎 Dados atuais de {nome_atual}:')
        print(f"   Valor da hora: R$ {dados_atuais['valor_hora']:.2f}")

        print('\nO que você deseja alterar?')
        print('1 - Nome')
        print('2 - Valor da hora')
        print('3 - Sair')

        opcao = input('Digite o número da opção desejada: ').strip()

        if opcao == '1':
            while True:
                novo_nome = input('Digite o novo nome do funcionário: ').strip().upper()
                if not novo_nome:
                    print('⚠️ O nome não pode estar vazio.')
                elif novo_nome in funcionarios:
                    print(f'⚠️ O nome "{novo_nome}" já está em uso. Tente outro.')
                else:
                    # Atualiza o dicionário com o novo nome
                    funcionarios[novo_nome] = funcionarios.pop(nome_atual)
                    print(f'✅ Nome do funcionário "{nome_atual}" alterado para "{novo_nome}".\n')
                    # A variável que guarda o nome atual precisa ser atualizada
                    nome_atual = novo_nome
                    break

        elif opcao == '2':
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

        elif opcao == '3':
            print('Saindo da alteração.')
            return

        else:
            print('Opção inválida. Por favor, digite 1, 2 ou 3.')

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
    for nome in funcionarios:
        valor_hora = funcionarios[nome]['valor_hora']
        print(f'Nome: {nome}')
        print(f'Valor da hora: R$ {valor_hora:.2f}')
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
            print('Encerrando o sistema... Até logo!')
            print('=' * 50)
            break
        else:
            print('Opção inválida! Tente novamente.')

        # Espera o usuário pressionar Enter apenas se não for a opção 'Sair'
        if opcao != '6':
            input('\nPressione Enter para continuar...')
            
# Chamando a função pra iniciar o sistema
rodar_programa()