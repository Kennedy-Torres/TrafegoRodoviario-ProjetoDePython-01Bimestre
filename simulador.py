from Carro import Carro
from Onibus import Onibus
from Caminhao import Caminhao


meu_carro = Carro("ABC-1234", "Fusca", 120, "São Paulo", "Rio de Janeiro")
caminhao = Caminhao("ccc-333", "Actros 2651", 240, "São Paulo", "Rio Grande do Sul")


#meu_carro.acelerar(80)
#meu_carro.acelerar(121)
#meu_carro.desacelerar(77)
meu_carro.velocimentro(12)
meu_carro.velocimentro(20)
meu_carro.velocimentro(9)
meu_carro.velocimentro(5)
meu_carro.velocimentro(0)
meu_carro.velocimentro(-29)
meu_carro.velocimentro(-69)
meu_carro.velocimentro(12)


caminhao.velocimentro(30)