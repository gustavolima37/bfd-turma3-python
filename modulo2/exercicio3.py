class Carro:
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano
    
    def __str__(self):
        return f'Modelo: {self.modelo} - Ano: {self.ano}'

    def ligar(self):
        return 'Carro ligado'


carro = Carro('Pegeot', 1980)
print(carro)
print(carro.ligar())
