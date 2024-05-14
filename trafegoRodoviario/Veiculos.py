class Veiculos:
    __slots__ =['_tipo','_placa','_modelo','_velocidadeMaxima','_cidadeAtual','_cidadeDestino']
    
    def __init__(self, tipo, placa, modelo, velocidadeMaxima, cidadeAtual, cidadeDestino):
        self._tipo = tipo;
        self._placa = placa;
        self._modelo = modelo;
        self._velocidadeMaxima = velocidadeMaxima;
        self._velocidadeAtual = 0; 
        self._cidadeAtual = cidadeAtual;
        self._cidadeDestino = cidadeDestino;
        
    
    # consulta a velocidade atual do veiculo
    @property 
    def acelerar(self):
        return self._velocidadeAtual
    
    @velocidade_atual.setter
    def acelerar(self,novaVelocidade):
        if(novaVelocidade<self.velocidadeMaxima):
            self._velocidadeAtual = novaVelocidade
            print(f"{self._tipo} de placa {self._placa} acelerou e está com velocidade de {self._velocidadeAtual} KM/H.")
        #elif(novaVelocidade>=self.velocidadeMaxima):
        else:
            self._velocidadeAtual = self._velocidadeMaxima # trava, nao permite ultrapassar a velocidadeMaxima
            print(f"{self._tipo} de placa {self._placa} acelerou e está com velocidade de {self._velocidadeAtual} KM/H.")
            
        
        
    
    #def desacelerar():
    
    #def mudar_de_faixa():
    # só pode mudar de faixa se o respectivo veiculo da faixa desacelerar
       