class SistemaController:
    # Construtor, uma lista de objetos
    def __init__(self):
        self.clientes = []
        self.compras = []

    #Cliente - adicionar e listar
    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def listar_clientes(self):
        return self.clientes

    #Compras - adicionar e listar
    def adicionar_compra(self, compra):
        self.compras.append(compra)

    def listar_compras(self):
        return self.compras