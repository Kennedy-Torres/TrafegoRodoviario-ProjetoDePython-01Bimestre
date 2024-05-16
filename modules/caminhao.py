from modules.veiculos import Veiculos


class Caminhao(Veiculos):
    def __init__(self, **kargs):
        try:
            super().__init__(tipo='Caminhao', **kargs)
        except KeyError as e:
            raise ValueError(f'Opa, faltou um argumento do tipo {e}') from e


if __name__ == '__main__':
    print(Caminhao(
        placa= 'DDD-5666',
        modelo= 'Volvo FH 540',
        velocidade_maxima= 120,
        velocidade_atual= 60,
        cidade_atual= 'São Paulo',
        cidade_destino= 'Rio de Janeiro'
    ))