from automoveis.Veiculos import Veiculos

class Caminhao(Veiculos):
    def __init__(self, placa, modelo, velocidadeMaxima):
        super().__init__("Caminhao", placa, modelo, velocidadeMaxima)