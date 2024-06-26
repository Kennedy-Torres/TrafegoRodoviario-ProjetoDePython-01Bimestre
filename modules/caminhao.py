"""Modulo Caminhao"""
from modules.veiculos import Veiculos


class Caminhao(Veiculos):
    """_summary_

    Args:
        Veiculos (_type_): _description_
    """
    def __init__(self, **kargs):
        try:
            super().__init__(tipo='Caminhao', **kargs)
        except KeyError as e:
            raise ValueError(f'Opa, faltou um argumento do tipo {e}') from e


if __name__ == '__main__':
    print(Caminhao(
        placa='DDD-5666',
        modelo='Volvo FH 540',
        velocidade_maxima=120,
        velocidade_atual=60,
        faixa_atual=3,  # inicializa o caminhao na faixa 3
        posicao=0,
    ))
