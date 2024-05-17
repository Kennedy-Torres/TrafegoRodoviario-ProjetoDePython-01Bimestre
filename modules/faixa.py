"""Modulo Faixas"""
class Faixa:
    """_summary_
    """
    def __init__(self, id_faixa):
        self.id_faixa = id_faixa
        self.veiculos = {}

    def adicionar_veiculo_em_faixa(self, veiculo) -> None:
        """_summary_

        Args:
            veiculo (_type_): _description_
        """
        self.veiculos[veiculo.nome_att('placa')] = veiculo

    def remover_veiculo_da_faixa(self, veiculo) -> None:
        """_summary_

        Args:
            veiculo (_type_): _description_
        """
        if veiculo.nome_att('placa') in self.veiculos:
            del self.veiculos[veiculo.nome_att('placa')]

    def posicao_esta_livre(self, posicao) -> bool:
        """_summary_

        Args:
            posicao (_type_): _description_

        Returns:
            bool: _description_
        """
        for veiculo in self.veiculos.values():
            if veiculo.pos_atual_na_estrada == posicao:
                return False
        return True

    def __str__(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """
        return f"  -Faixa {self.id_faixa} com {len(self.veiculos)} veículo(s)"
