from trafegoRodoviario.Veiculos import Veiculos

class Carro(Veiculos):
    def __init__(self, modelo, velocidadeMaxima, cidadeAtual, cidadeDestino):
        super.__init__("Carro", modelo, velocidadeMaxima, cidadeAtual, cidadeDestino)