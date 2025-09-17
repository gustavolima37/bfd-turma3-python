# main.py

from modelos import casas_sustentaveis

def listar_por_tipo(tipo_desejado):
    """Filtra e imprime habitações de um tipo específico."""
    tipo_desejado = tipo_desejado.upper()
    print(f"\n--- Habitações do Tipo: {tipo_desejado} ---")
    if tipo_desejado in casas_sustentaveis:
        for casa in casas_sustentaveis[tipo_desejado]:
            print("-----------------------------------")
            print(casa)
    else:
        print(f"Tipo '{tipo_desejado}' não encontrado.")
    print("-----------------------------------\n")

def menu_principal():
    """Exibe um menu interativo para o usuário."""
    while True:
        print("---------------------------------------")
        print("  MENU - Habitações Sustentáveis")
        print("---------------------------------------")
        print("1. Mostrar casas - BIOCONSTRUÇÃO")
        print("2. Mostrar casas - MODULARES")
        print("3. Mostrar casas - PASSIVAS")
        print("4. Mostrar casas - RECICLADAS")
        print("5. Sair")
        print("---------------------------------------")
        
        escolha = input("Digite o número da sua escolha: ")

        if escolha == '1':
            listar_por_tipo("BIOCONSTRUÇÃO")
        elif escolha == '2':
            listar_por_tipo("MODULAR")
        elif escolha == '3':
            listar_por_tipo("PASSIVA")
        elif escolha == '4':
            listar_por_tipo("RECICLADA")
        elif escolha == '5':
            print("Encerrando Sistema.")
            break
        else:
            print("Escolha inválida. Por favor, tente novamente.")
            
# Inicia o menu quando o script é executado
if __name__ == "__main__":
    menu_principal()