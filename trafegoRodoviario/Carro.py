from Veiculos import Veiculos

class Carro(Veiculos):
    def __init__(self, placa, modelo, velocidadeMaxima, cidadeAtual, cidadeDestino):
        super().__init__("Carro", placa, modelo, velocidadeMaxima, cidadeAtual, cidadeDestino)