from modules.faixa import Faixa
from print_cores import Cores

class Estrada:
    def __init__(self, num_faixas, nome_da_estrada):
        self.faixas = [Faixa(i) for i in range(1, num_faixas + 1)]
        self.nome_da_estrada = nome_da_estrada

    def adicionar_veiculo(self, veiculo, id_faixa):
        self.faixas[id_faixa - 1].adicionar_veiculo(veiculo)

    def atualizar_faixa(self, veiculo, faixa_atual, nova_faixa):
        self.faixas[faixa_atual - 1].remover_veiculo(veiculo)
        self.faixas[nova_faixa - 1].adicionar_veiculo(veiculo)

    def verificar_posicao_livre(self, id_faixa, posicao):
        return self.faixas[id_faixa - 1].verificar_posicao_livre(posicao)

    def __str__(self):
        estado_faixas = "\n".join(str(faixa) for faixa in self.faixas)
        return f'-> {Cores.MARROM}Estado da Estrada {Cores.SUBLINHADO}{self.nome_da_estrada}:{Cores.RESET} \n{estado_faixas} {Cores.RESET}'