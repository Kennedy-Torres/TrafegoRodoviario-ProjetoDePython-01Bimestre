from time import sleep
from random import randint
from print_cores import Cores


class Veiculos:

    # def __init__(self, tipo:str, placa:str, modelo:str, velocidadeMaxima:str, cidadeAtual:str, cidadeDestino:str):
    def __init__(self, **kargs):
        self._tipo = kargs['tipo']
        self._placa = kargs['placa']
        self._modelo = kargs['modelo']
        self._velocidade_maxima = kargs['velocidade_maxima']
        self._velocidade_atual = kargs['velocidade_atual']
        #self._cidade_atual = kargs['cidade_atual']
        #self._cidade_destino = kargs['cidade_destino']
        self._faixa_atual = kargs['faixa_atual']
        self._posicao = kargs['posicao'] # posicao relacionada ao local que o veiculo esta na estrada

    def nome_att(self, atributo:str) -> str:
        #return Veiculos.__dict__[f'_{atributo}']
        return self.__dict__[f'_{atributo}']
    
    # consulta e define a faixa atual
    @property
    def faixa(self):
        return self._faixa_atual
    
    @faixa.setter
    def faixa(self, nova_faixa):
        self._faixa_atual = nova_faixa
        
    
    @property
    def pos_atual_na_estrada(self):
        return self._posicao

    @pos_atual_na_estrada.setter
    def pos_atual_na_estrada(self, nova_posicao):
        self._posicao = nova_posicao
        
    # consulta e definide velocidade máxima do veiculo
    @property
    def vel_maxima(self):
        return self._velocidade_maxima


    @vel_maxima.setter
    def vel_maxima(self, velocidade_maxima:int):
        print(f"{self._tipo} de modelo {self._modelo} alterou sua velocidade máxima de {self._velocidade_maxima} KM/H para {velocidade_maxima} KM/H")
        self._velocidade_maxima = velocidade_maxima

    # consulta e definide velocidade atual do veiculo
    @property
    def vel_atual(self):
        return self._velocidade_atual


    @vel_atual.setter
    def vel_atual(self, velocidade_atual:int):
        print(f"({self.nome_att('tipo')}) - {self.nome_att('modelo')} de placa {self.nome_att('placa')} passou de:\n   -> {self._velocidade_atual} KM/H para {velocidade_atual} KM/H.")
        self.atualizar_posicao(self._velocidade_atual, velocidade_atual)
        self._velocidade_atual = velocidade_atual
        


    def acelerar(self, velocidade_atual:int):
        while True:
            vel_random = randint(velocidade_atual, self.vel_maxima+10)
            sleep(0.5)
            if velocidade_atual < vel_random:
                return vel_random


    def desacelerar(self, velocidade_atual:int):
        while True:
            vel_random = randint(0, velocidade_atual)
            sleep(0.5)
            if vel_random < velocidade_atual:
                return vel_random
            elif vel_random <= 0:
                return 0
            


    '''def velocimentro(self, nova_vel:int):
        if nova_vel > self._velocidade_atual:
            self.acelerar(nova_vel)
        else:
            self.desacelerar(nova_vel)
    '''

    def mudar_de_faixa(self, estrada, nova_faixa):
        if estrada.verificar_posicao_livre(nova_faixa, self.pos_atual_na_estrada):
            print(f"({self.nome_att('tipo')}) - {self.nome_att('modelo')} de placa {self.nome_att('placa')} mudando da faixa {self._faixa_atual} para faixa {nova_faixa} na posicao {self.pos_atual_na_estrada} km da estrada {estrada._nome_da_estrada}")
            
            estrada.atualizar_faixa(self, self._faixa_atual, nova_faixa)
            self._faixa_atual = nova_faixa
        else:
            print(f"-> {Cores.VERMELHO_CLARO}({self._tipo}) - {self.nome_att('modelo')} de placa {self._placa} não pode mudar para a faixa {nova_faixa} pois a posição {self.pos_atual_na_estrada} está ocupada{Cores.RESET}")

    def atualizar_posicao(self, velocidade_inicial, velocidade_final):
        tempo = 1  # duracao de 1hora para aumentar de uma velocidade x para y ... deixei estatico para facilitar...
        velocidade_media = (velocidade_inicial + velocidade_final) / 2
        deslocamento = (velocidade_media * (tempo))
        nova_posicao = self._posicao + deslocamento
        print(f"   -> Da posição {self._posicao} km para {nova_posicao} km") # posicao q o veic está dentro da estrada
        self._posicao = nova_posicao
        
    