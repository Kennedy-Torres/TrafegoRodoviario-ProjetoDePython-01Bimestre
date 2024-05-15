from automoveis.Veiculos import Veiculos

class Onibus(Veiculos):
    def __init__(self, placa, modelo, velocidadeMaxima):
        super().__init__("Onibus", placa, modelo, velocidadeMaxima)