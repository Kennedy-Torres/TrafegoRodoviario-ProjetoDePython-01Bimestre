from modules.veiculos import Veiculos


class Caminhao(Veiculos):
    def __init__(self, **kargs):
        try:
            super().__init__(tipo='Caminhao', **kargs)
        except KeyError as e:
            raise ValueError(f'Opa, faltou um argumento do tipo {e}') from e
