"""---"""
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
        cidade_atual= 'São Paulo',
        cidade_destino= 'Rio de Janeiro'
    ))
