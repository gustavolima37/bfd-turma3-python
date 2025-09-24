# visao.py
from modelo import Cliente, Produto, Compra  # <-- Adicionada a classe Produto
from controle import SistemaController

def main():
    sistema = SistemaController()

    # Criando objetos de Cliente
    c1 = Cliente(1, 'Maria Silva')
    c2 = Cliente(2, 'João Souza')
    sistema.adicionar_cliente(c1)
    sistema.adicionar_cliente(c2)
    
    # Criando objetos de Produto
    p1 = Produto(1, 'Notebook', 12000.00)
    p2 = Produto(2, 'Mouse Gamer', 150.00)
    p3 = Produto(3, 'Teclado Mecânico', 350.00)

    # Criando a primeira compra e associando os objetos corretos
    compra1 = Compra(101, '2025-09-15', c1) # <-- Passando o objeto c1
    compra1.adicionar_item(p1, 1)           # <-- Adicionando um produto
    compra1.adicionar_item(p2, 2)           # <-- Adicionando outro produto
    
    # Criando a segunda compra e associando os objetos corretos
    compra2 = Compra(102, '2025-09-16', c2) # <-- Passando o objeto c2
    compra2.adicionar_item(p3, 1)           # <-- Adicionando um produto

    sistema.adicionar_compra(compra1)
    sistema.adicionar_compra(compra2)
    
    # Exibindo resultados
    print('-'*50)
    print('\n=== CLIENTES ===')
    for cliente in sistema.listar_clientes():
        print(cliente)
    print('-'*50)

    print('\n=== COMPRAS ===')
    for compra in sistema.listar_compras():
        print(compra)
    print('-'*50)


if __name__ == '__main__':
    main()