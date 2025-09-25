class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    def __str__(self):
        result = float(self.largura) * float(self.altura)
        return f'A area é {result:.2f}'


area = Retangulo(20,10)
print(area)