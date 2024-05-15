class Rodovia:
    
    def __init__(self, nome,cidade_origem, cidade_destino, numero_de_faixas):
        self._nome = nome
        self._cidade_origem = cidade_origem
        self._cidade_destino = cidade_destino
        self._numero_de_faixas = numero_de_faixas
        self._veiculos = []

    def adicionar_veiculo(self, veiculo):
        veiculo._cidadeAtual = self._cidade_origem
        veiculo._cidadeDestino = self._cidade_destino
        self._veiculos.append(veiculo)
        print(f"{veiculo._tipo} de placa {veiculo._placa} entrou na rodovia {self._nome} sentido {self._cidade_origem} para {self._cidade_destino}.")

    def mostrar_veiculos(self):
        print("""\n================= DADOS DOS VEICULOS NAS RODOVIA ======================""")
        for veiculo in self._veiculos:
            print(f"""{veiculo._tipo} de placa {veiculo._placa}:
    Rodovia {self._nome} - origem:{self._cidade_origem}, destino:{self._cidade_destino} 
    Faixa atual: {veiculo._faixa}
    Velocidade atual: {veiculo.velocidadeAtual} KM/H.""")