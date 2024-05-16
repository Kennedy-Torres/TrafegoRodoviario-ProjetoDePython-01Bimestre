"""---"""
from modules.veiculos import Veiculos


class Onibus(Veiculos):
    def __init__(self, **kargs):
        try:
            super().__init__(tipo='Onibus', **kargs)
        except KeyError as e:
            raise ValueError(f'Opa, faltou um argumento do tipo {e}') from e


if __name__ == '__main__':
    print(Onibus(
        placa= 'ABC-1234',
        modelo= 'Mini-Bus',
        velocidade_maxima= 80,
        velocidade_atual= 60,
        cidade_atual= 'São Paulo',
        cidade_destino= 'Rio de Janeiro',
        faixa_atual= 2, # inicializa o onibus na faixa 2
        posicao= 0 
    ))
