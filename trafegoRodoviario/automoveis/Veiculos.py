class Veiculos:
    #__slots__ =['_tipo','_placa','_modelo','_velocidadeMaxima','_cidadeAtual','_cidadeDestino']
    
    def __init__(self, tipo, placa, modelo, velocidadeMaxima):
        self._tipo = tipo
        self._placa = placa
        self._modelo = modelo
        self._velocidadeMaxima = velocidadeMaxima
        self._velocidadeAtual = 0
        self._cidadeAtual = None
        self._cidadeDestino = None
        self._faixa = 1 # veiculos inicializados na faixa 1 
        
        
    # consulta e definide velocidade máxima do veiculo
    @property 
    def velocidadeMaxima(self):
        return self._velocidadeMaxima
    
    @velocidadeMaxima.setter
    def velocidadeMaxima(self,velocidadeMaxima):
        print(f"{self._tipo} de modelo {self._modelo} alterou sua velocidade máxima de {self._velocidadeMaxima} KM/H para {velocidadeMaxima} KM/H")
        self._velocidadeMaxima = velocidadeMaxima
        
    # consulta e definide velocidade atual do veiculo
    @property
    def velocidadeAtual(self):
        return self._velocidadeAtual
    
    @velocidadeAtual.setter
    def velocidadeAtual(self, velocidadeAtual):
        print(f"{self._tipo} de placa {self._placa} passou de {self._velocidadeAtual} KM/H para {velocidadeAtual} KM/H")
        self._velocidadeAtual = velocidadeAtual
    
    
    def acelerar(self,novaVelocidade):
        if(novaVelocidade <= self._velocidadeMaxima):
            print("Acelerando...")
            self.velocidadeAtual= novaVelocidade
        else:
            print(f"Velocidade máxima atingida; ( passou de {self.velocidadeAtual} KM/H para {self.velocidadeMaxima} KM/H ).")
            self._velocidadeAtual = self._velocidadeMaxima # trava, nao permite ultrapassar a velocidadeMaxima
            
    def desacelerar(self, novaVelocidade):
        if (novaVelocidade < self._velocidadeAtual and novaVelocidade>=0):
            print("Desacelerando...")
            self.velocidadeAtual = novaVelocidade
        elif(novaVelocidade<0 and novaVelocidade> (-self.velocidadeMaxima/2) ): # por convensão adotamos o limite negativo como a metade do limite positivo
            print("Dando ré...")
            self.velocidadeAtual = novaVelocidade
        else:
            print(f"""\n======================= ATENÇÃO =======================
Velocidade máxima de ré atingida. ( Limite: {-self.velocidadeMaxima/2} KM/H)
=======================================================""") 
            self.velocidadeAtual = -self.velocidadeMaxima/2
            
    def velocimentro(self,novaVelocidade):
        if (novaVelocidade > self._velocidadeAtual):
            self.acelerar(novaVelocidade)
        else:
            self.desacelerar(novaVelocidade)
    
    
    
    def mudar_de_faixa(self, nova_faixa, rodovia):
        if 1 <= nova_faixa <= rodovia._numero_de_faixas:
            if self._faixa != nova_faixa:
                #print("Mudando de faixa...")
                print(f"""Mudando de faixa...
{self._tipo} de placa {self._placa} mudou da faixa {self._faixa} para a faixa {nova_faixa}.""")
                self._faixa = nova_faixa
            else:
                print("...")
                print(f"{self._tipo} de placa {self._placa} já está na faixa {nova_faixa}.")
        else:
            print(f"""Faixa inválida...
{self._tipo} de placa {self._placa} não conseguiu mudar de faixa; A rodovia possui apenas {rodovia._numero_de_faixas} faixas.""")
       