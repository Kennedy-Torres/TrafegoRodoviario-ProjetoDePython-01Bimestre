from Veiculos import Veiculos

class Caminhao(Veiculos):
    def __init__(self, placa, modelo, velocidadeMaxima, cidadeAtual, cidadeDestino):
        super().__init__("Caminhao", placa, modelo, velocidadeMaxima, cidadeAtual, cidadeDestino)