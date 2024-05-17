"""Modulo Estrada"""
from print_cores import Cores

from modules.faixa import Faixa


class Estrada:
    """_summary_
    """

    def __init__(self, **kargs):
        self._num_faixas = kargs.get('num_faixas', 1)
        self._nome_da_estrada = kargs.get('nome_da_estrada')
        self._tamanho = kargs.get('tamanho', 0)  # default 0...
        self._cidade_inic = kargs.get('cidade_inicial')
        self._cidade_final = kargs.get('cidade_final')
        self.faixas = [Faixa(i) for i in range(1, self._num_faixas + 1)]

    def nome_att_da_estrada(self, atributo: str) -> str:
        """_summary_

        Args:
            atributo (str): _description_

        Returns:
            str: _description_
        """
        return self.__dict__[f'_{atributo}']

    def adicionar_veiculo(self, veiculo, id_faixa) -> None:
        """_summary_

        Args:
            veiculo (_type_): _description_
            id_faixa (_type_): _description_
        """
        print(f'{Cores.MARROM}', veiculo.nome_att('modelo'), 'entrou na estrada',
              self.nome_att_da_estrada('nome_da_estrada'), f'{Cores.RESET}')
        self.faixas[id_faixa - 1].adicionar_veiculo_em_faixa(veiculo)

    def remov_veiculo(self, veiculo) -> None:
        """_summary_

        Args:
            veiculo (_type_): _description_
        """
        self.faixas[veiculo.faixa - 1].remover_veiculo_da_faixa(veiculo)
        print(f'{Cores.VERMELHO_CLARO}', veiculo.nome_att('modelo'), 'saiu da estrada',
              self.nome_att_da_estrada('nome_da_estrada'), f'{Cores.RESET}')

    def atualizar_faixa(self, veiculo, faixa_atual, nova_faixa) -> None:
        """_summary_

        Args:
            veiculo (_type_): _description_
            faixa_atual (_type_): _description_
            nova_faixa (_type_): _description_
        """
        self.faixas[faixa_atual - 1].remover_veiculo_da_faixa(veiculo)
        self.faixas[nova_faixa - 1].adicionar_veiculo_em_faixa(veiculo)

    def verificar_posicao_livre(self, id_faixa, posicao) -> str:
        """_summary_

        Args:
            id_faixa (_type_): _description_
            posicao (_type_): _description_

        Returns:
            str: _description_
        """
        return self.faixas[id_faixa - 1].posicao_esta_livre(posicao)

    def verificar_fim_estrada(self, veiculo) -> bool:
        """_summary_

        Args:
            veiculo (_type_): _description_

        Returns:
            bool: _description_
        """
        if veiculo.pos_atual_na_estrada >= self.nome_att_da_estrada('tamanho'):
            print(f'{Cores.VERDE_CLARO}({veiculo.nome_att("tipo")}) - {veiculo.nome_att("modelo")} de placa {veiculo.nome_att("placa")} chegou em: {self.nome_att_da_estrada("cidade_final")}!{Cores.RESET}')
            return True
        return False

    def __str__(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        estado_faixas = "\n".join(str(faixa) for faixa in self.faixas)
        return f'{Cores.NEGRITO}Estado da Estrada {Cores.SUBLINHADO}{self.nome_att_da_estrada("nome_da_estrada")}:{Cores.RESET} \n{estado_faixas} {Cores.RESET}'
