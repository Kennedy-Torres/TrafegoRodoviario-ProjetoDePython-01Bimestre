class Faixa:
    def __init__(self, id_faixa):
        self.id_faixa = id_faixa
        self.veiculos = []

    def adicionar_veiculo(self, veiculo):
        self.veiculos.append(veiculo)

    def remover_veiculo(self, veiculo):
        self.veiculos.remove(veiculo)

    def verificar_posicao_livre(self, posicao):
        for veiculo in self.veiculos:
            if veiculo.pos_atual_na_estrada == posicao:
                return False
        return True

    def __str__(self):
        return f"  -Faixa {self.id_faixa} com {len(self.veiculos)} veículo(s)"
