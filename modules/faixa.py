class Faixa:
    def __init__(self, id_faixa):
        self.id_faixa = id_faixa
        #self.veiculos = []
        self.veiculos = {}

    def adicionar_veiculo_emFaixa(self, veiculo):
        #self.veiculos.append(veiculo)
        self.veiculos[veiculo.nome_att('placa')] = veiculo

    def remover_veiculo_daFaixa(self, veiculo):
        #self.veiculos.remove(veiculo)
        if veiculo.nome_att('placa') in self.veiculos:
            del self.veiculos[veiculo.nome_att('placa')]

    def posicao_esta_livre(self, posicao):
        for veiculo in self.veiculos.values():
            if veiculo.pos_atual_na_estrada == posicao:
                return False
        return True

    def __str__(self):
        return f"  -Faixa {self.id_faixa} com {len(self.veiculos)} veículo(s)"
