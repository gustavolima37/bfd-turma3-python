# modelos.py

class HabitacaoSustentavel:
    """Representa uma habitação com foco em sustentabilidade."""
    def __init__(self, nome, tipo, data_construcao, localizacao, objetivo, sistema_energia):
        self.nome = nome
        self.tipo = tipo
        self.data_construcao = data_construcao
        self.localizacao = localizacao
        self.objetivo = objetivo
        self.sistema_energia = sistema_energia

    def __str__(self):
        """Retorna uma representação em string do objeto para impressão."""
        return (f"Nome: {self.nome}\n"
                f"Tipo: {self.tipo}\n"
                f"Localização: {self.localizacao}\n"
                f"Sistema de Energia: {self.sistema_energia}\n"
                f"Objetivo: {self.objetivo}\n")

# Dados das habitações
casas_sustentaveis = {
    "BIOCONSTRUÇÃO": [
        HabitacaoSustentavel(nome="Casa Terra Viva", tipo="BIOCONSTRUÇÃO", data_construcao="15/05/2023", objetivo="Materiais locais e baixo impacto.", localizacao="Serra Gaúcha, RS", sistema_energia="Solar fotovoltaica"),
        HabitacaoSustentavel(nome="Refúgio de Adobe", tipo="BIOCONSTRUÇÃO", data_construcao="20/09/2022", objetivo="Eficiência térmica com tijolos de adobe.", localizacao="Chapada Diamantina, BA", sistema_energia="Eólica de pequeno porte")
    ],
    "MODULAR": [
        HabitacaoSustentavel(nome="EcoCube Modular", tipo="MODULAR", data_construcao="10/01/2024", objetivo="Estrutura pré-fabricada de madeira e aço.", localizacao="Litoral Norte, SP", sistema_energia="Solar térmica"),
        HabitacaoSustentavel(nome="Módulo Habitat Verde", tipo="MODULAR", data_construcao="25/03/2023", objetivo="Captação de água da chuva.", localizacao="Interior de Minas Gerais, MG", sistema_energia="Solar fotovoltaica")
    ],
    "PASSIVA": [
        HabitacaoSustentavel(nome="Vento e Luz", tipo="PASSIVA", data_construcao="08/07/2022", objetivo="Design que maximiza ventilação natural.", localizacao="Planalto Central, DF", sistema_energia="Nenhum (design passivo)"),
        HabitacaoSustentavel(nome="Céu Azul Passiva", tipo="PASSIVA", data_construcao="14/11/2023", objetivo="Isolamento térmico de alta performance.", localizacao="Vale do Paraíba, SP", sistema_energia="Solar fotovoltaica (apoio) e design passivo")
    ],
    "RECICLADA": [
        HabitacaoSustentavel(nome="Casa dos Containers", tipo="RECICLADA", data_construcao="01/04/2023", objetivo="Estrutura principal feita de containers.", localizacao="Região Metropolitana, RJ", sistema_energia="Solar fotovoltaica"),
        HabitacaoSustentavel(nome="Habitat de Pneus", tipo="RECICLADA", data_construcao="30/06/2022", objetivo="Uso de pneus e garrafas plásticas.", localizacao="Sertão Nordestino, PE", sistema_energia="Eólica de pequeno porte")
    ]
}