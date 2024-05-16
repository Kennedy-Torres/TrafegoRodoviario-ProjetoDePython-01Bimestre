class Rodovia:
    
    def __init__(self, nome,cidade_origem, cidade_destino, numero_de_faixas, tamanho_da_pista):
        self._nome = nome
        self._cidade_origem = cidade_origem
        self._cidade_destino = cidade_destino
        self._numero_de_faixas = numero_de_faixas
        self._tamanho_da_pista = tamanho_da_pista
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
    Posição: {veiculo._posicao:.2f} KM 
    Velocidade atual: {veiculo.velocidadeAtual} KM/H.""")
        print("""=========================================================================""")
    def atualizar_posicao_do_veiculo_na_rodovia(self, minutos):
        for veiculo in self._veiculos:
            distancia_percorrida = veiculo._velocidadeAtual * minutos / 60  # km por minuto
            veiculo._posicao += distancia_percorrida
            if veiculo._posicao > self._tamanho_da_pista:
                veiculo._posicao = self._tamanho_da_pista  # veículo atinge o destino
                print(f"{veiculo._tipo} de placa {veiculo._placa} chegou ao destino.")
            
            #testes
            #print(f"{veiculo._tipo} de placa {veiculo._placa} percorreu {distancia_percorrida:.2f} km em {minutos} minutos e está na posição {veiculo._posicao:.2f} km.")
            
        self.verificar_colisao_traseira()
            
            
    def verificar_colisao_lateral(self, veiculo, nova_faixa, nova_posicao):
        for v in self._veiculos:
            if v != veiculo and v._faixa == nova_faixa and v._posicao == nova_posicao:
                return True
        return False
    
    def verificar_colisao_traseira(self):
        for i, veiculo1 in enumerate(self._veiculos):
            for veiculo2 in self._veiculos[i + 1:]:
                if veiculo1._faixa == veiculo2._faixa:
                    if(veiculo1._posicao == veiculo2._posicao and (veiculo1._posicao != self._tamanho_da_pista or veiculo2._posicao != self._tamanho_da_pista)):  # considerando os veiculos como objetos puntiformes e que no destino final eles não se colidem
                        print(f"""Colisão traseira detectada...
    {veiculo1._tipo} de placa {veiculo1._placa} colidiu com {veiculo2._tipo} de placa {veiculo2._placa} na faixa {veiculo1._faixa} na posição {veiculo1._posicao:.2f} km da rodovia {self._nome}.""")