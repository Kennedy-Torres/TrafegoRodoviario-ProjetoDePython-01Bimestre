from Veiculos import Veiculos

class Onibus(Veiculos):
    def __init__(self, placa, modelo, velocidadeMaxima, cidadeAtual, cidadeDestino):
        super().__init__("Onibus", placa, modelo, velocidadeMaxima, cidadeAtual, cidadeDestino)