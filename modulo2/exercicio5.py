class Funcionario:
    def __init__(self, nome, cargo):
        self.nome = nome
        self.cargo = cargo
    def apresentar(self):
        return f'Olá, sou {self.nome} e meu cargo é {self.cargo}.'
    
class Gerente(Funcionario):
    def __init__(self, nome, cargo, area):
        super().__init__(nome, cargo)
        self.area = area
    def apresentar(self):
        info_pai = super().apresentar()
        return f'{info_pai} Sou Gerente da área de {self.area}'


gerente = Gerente('Roberto', 'Gerente Frios', 'Açougue')
print(gerente.apresentar())