class Cliente:
    def __init__(self, id_cliente, nome):
        self.id_cliente = id_cliente
        self.nome = nome

    def __str__(self):
        return f'Cliente {self.id_cliente}: {self.nome}'

class Produto:
    def __init__(self, id_produto, nome, preco):
        self.id_produto = id_produto
        self.nome = nome
        self.preco = preco

class Compra:
    def __init__(self, id_compra, data_compra, cliente):
        self.id_compra = id_compra
        self.data_compra = data_compra
        self.cliente = cliente
        self.itens = []

    def adicionar_item(self, produto, quantidade):
        # Corrigido o nome da lista para 'self.itens'
        self.itens.append({'produto': produto, 'quantidade': quantidade})
        
    def valor_total(self):
        total = 0
        for item in self.itens:
            total += item['produto'].preco * item['quantidade']
        return total

    def __str__(self):
        desc = (f'Compra {self.id_compra} em {self.data_compra} ' # <-- Corrigido o espaço
                f'do(a) {self.cliente.nome}:\n')
        for item in self.itens:
            produto = item['produto']
            quantidade = item['quantidade']
            # Corrigida a formatação do preço
            desc += (f'  -> {quantidade} x {produto.nome} (R$ {produto.preco:.2f} cada)\n')
        
        desc += f'Total da compra: R$ {self.valor_total():.2f}'
        return desc

if __name__ == '__main__':
    # Criando objetos de Cliente
    cliente1 = Cliente(1, 'Rosas')
    cliente2 = Cliente(2, 'Orquideas')
    
    # Criando objetos de Produto
    produto1 = Produto(1, 'Notebook', 12000.00)
    produto2 = Produto(2, 'Mouse Gamer', 150.00)
    produto3 = Produto(3, 'Teclado Mecânico', 350.00)
    
    # Criando e populando a primeira compra
    compra1 = Compra(101, '2025-09-15', cliente1)
    compra1.adicionar_item(produto1, 1)
    compra1.adicionar_item(produto2, 2)

    # Criando e populando a segunda compra
    compra2 = Compra(102, '2025-09-16', cliente2)
    compra2.adicionar_item(produto3, 1)

    print(compra1)
    print('\n' + '='*30 + '\n')
    print(compra2)