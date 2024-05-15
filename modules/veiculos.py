from time import sleep
from random import randint


class Veiculos:
    # __slots__ =['_tipo','_placa','_modelo','_velocidadeMaxima','_cidadeAtual','_cidadeDestino']

    # def __init__(self, tipo:str, placa:str, modelo:str, velocidadeMaxima:str, cidadeAtual:str, cidadeDestino:str):
    def __init__(self, **kargs):
        self._tipo = kargs['tipo']
        self._placa = kargs['placa']
        self._modelo = kargs['modelo']
        self._velocidade_maxima = kargs['velocidade_maxima']
        self._velocidade_atual = kargs['velocidade_atual']
        self._cidade_atual = kargs['cidade_atual']
        self._cidade_destino = kargs['cidade_destino']

    def nome_att(self, atributo:str) -> str:
        return Veiculos.__dict__[f'_{atributo}']

    # consulta e definide velocidade máxima do veiculo
    @property
    def vel_maxima(self):
        return self._velocidade_maxima


    @vel_maxima.setter
    def vel_maxima(self, velocidade_maxima:int):
        print(f"{self._tipo} de modelo {self._modelo} alterou sua velocidade máxima de {
              self._velocidade_maxima} KM/H para {velocidade_maxima} KM/H")
        self._velocidade_maxima = velocidade_maxima

    # consulta e definide velocidade atual do veiculo
    @property
    def vel_atual(self):
        return self._velocidade_atual


    @vel_atual.setter
    def vel_atual(self, velocidade_atual:int):
        print(f"{self._tipo} de placa {self._placa} passou de {
              self._velocidade_atual} KM/H para {velocidade_atual} KM/H")
        self._velocidade_atual = velocidade_atual


    def acelerar(self, velocidade_atual:int):
        while True:
            vel_random = randint(velocidade_atual, self.vel_maxima+10)
            sleep(0.5)
            if velocidade_atual < vel_random:
                return vel_random


    def desacelerar(self, nova_vel:int):
        if nova_vel < self._velocidade_atual >= 0:
            print("Desacelerando...")
            self._velocidade_atual = nova_vel
        # por convensão adotamos o limite negativo como a metade do limite positivo
        elif nova_vel < 0 and nova_vel > (-self._velocidade_maxima/2):
            print("Dando ré...")
            self._velocidade_atual = nova_vel
        else:
            print(f"""
\n======================= ATENÇÃO =======================
Velocidade máxima de ré atingida. ( Limite: {-self._velocidade_maxima/2} KM/H)
=======================================================""")
            self._velocidade_atual = -self._velocidade_maxima/2


    def velocimentro(self, nova_vel:int):
        if nova_vel > self._velocidade_atual:
            self.acelerar(nova_vel)
        else:
            self.desacelerar(nova_vel)

    # def mudar_de_faixa():
    # uma das lógicas que podemos adotar só pode mudar de faixa se o respectivo veiculo da faixa desacelerar
