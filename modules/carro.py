"""Modulo Carro"""
from modules.veiculos import Veiculos


class Carro(Veiculos):
    """_summary_

    Args:
        Veiculos (_type_): _description_
    """
    def __init__(self, **kargs):
        try:
            super().__init__(tipo='Carro', **kargs)
        except KeyError as e:
            raise ValueError(f'Opa, faltou um argumento do tipo {e}') from e


if __name__ == '__main__':
    print(Carro(
        placa= 'ABC-1234',
        modelo= 'Fusca',
        velocidade_maxima= 120,
        velocidade_atual= 60,
        faixa_atual= 1, # inicializa o carro na faixa 1
        posicao= 0
    ))
