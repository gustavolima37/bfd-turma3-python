class Cliente:
    def __init__(self, nome):
        self.nome = nome
        
    def __str__(self):
        return f'Cliente: {self.nome}'
    
class Produto:
    def __init__(self, produto_nome, valor):
        self.produto_nome = produto_nome
        self.valor = valor
        
    def __str__(self):
        return f'Produto: {self.produto_nome} - R$ {self.valor}'
        
class Carrinho:
    def __init__(self):
        self.produtos = []
        
    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        
    def calcular_total(self):
        total = 0
        for i in self.produtos:
            total += i.valor
        return total
    
#Criação do cliente e produtos

cliente1 = Cliente('João')
produto1 = Produto('Arroz', 3.80)
produto2 = Produto('Feijão', 8.00)
produto3 = Produto('Macarrão', 2.75)

#Criação do Carrinho

carrinho_joao = Carrinho()

#Adicionando no carrinho

carrinho_joao.adicionar_produto(produto1)
carrinho_joao.adicionar_produto(produto1)
carrinho_joao.adicionar_produto(produto1)
carrinho_joao.adicionar_produto(produto2)
carrinho_joao.adicionar_produto(produto3)

#Calcular e exibir 

total_de_compra = carrinho_joao.calcular_total()

print(cliente1)

print('--- Resumo da Compra ---')
for item in carrinho_joao.produtos:
    print(f'-> {item}')
    
print(f'\nTotal da compra: R$ {total_de_compra:.2f}')