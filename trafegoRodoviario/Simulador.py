from automoveis.Carro import Carro
from automoveis.Onibus import Onibus
from automoveis.Caminhao import Caminhao

from rodovias.Rodovia import Rodovia


carro1 = Carro("ABC-1234", "Fusca", 120)
caminhao1 = Caminhao("ccc-333", "Actros 2651", 240)
onibus1 = Onibus("ppp-090","Marechal",150)
rodovia1 = Rodovia("três patinhos","SP", "RJ", 3)

print("""================= ADD VEICULOS NA RODOVIA ======================""")
rodovia1.adicionar_veiculo(carro1)
rodovia1.adicionar_veiculo(caminhao1)
rodovia1.adicionar_veiculo(onibus1)
print("================================================================\n")

carro1.mudar_de_faixa(2,rodovia1)
caminhao1.mudar_de_faixa(1,rodovia1)
onibus1.mudar_de_faixa(4,rodovia1)

'''
TESTES DO VELOCIMETRO
'''
#carro1.acelerar(80)
#carro1.acelerar(121)
#carro1.desacelerar(77)
'''
carro1.velocimentro(12)
carro1.velocimentro(20)
carro1.velocimentro(9)
carro1.velocimentro(5)
carro1.velocimentro(0)
carro1.velocimentro(-29)
carro1.velocimentro(-69)
carro1.velocimentro(12)
caminhao.velocimentro(30)
'''
# ----
# ----

carro1.velocimentro(12)
caminhao1.velocimentro(30)
onibus1.velocimentro(70)



rodovia1.mostrar_veiculos()