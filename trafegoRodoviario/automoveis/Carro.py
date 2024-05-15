from automoveis.Veiculos import Veiculos

class Carro(Veiculos):
    def __init__(self, placa, modelo, velocidadeMaxima):
        super().__init__("Carro", placa, modelo, velocidadeMaxima)