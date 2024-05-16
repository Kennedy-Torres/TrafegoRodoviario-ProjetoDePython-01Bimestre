from automoveis.Carro import Carro
from automoveis.Onibus import Onibus
from automoveis.Caminhao import Caminhao

from rodovias.Rodovia import Rodovia


carro1 = Carro("ABC-1234", "Fusca", 120)
carro2 = Carro("QQR-341", "Astra", 220)
caminhao1 = Caminhao("ccc-333", "Actros 2651", 240)
onibus1 = Onibus("ppp-090","Marechal",150)
rodovia1 = Rodovia("três patinhos","SP", "RJ", 3, 400)
rodovia2 = Rodovia("Galho fraco","MG", "RS", 2, 800)

print("""================= ADD VEICULOS NA RODOVIA ======================""")
rodovia1.adicionar_veiculo(carro1)
rodovia1.adicionar_veiculo(caminhao1)
rodovia1.adicionar_veiculo(onibus1)
rodovia2.adicionar_veiculo(carro2)
print("================================================================\n")

carro1.mudar_de_faixa(2,rodovia1)
#caminhao1.mudar_de_faixa(3,rodovia1)
#onibus1.mudar_de_faixa(3,rodovia1)

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

# 30 minutos iniciais com velocidade constante de ...12...30...70
carro1.velocimentro(12)
caminhao1.velocimentro(30)
onibus1.velocimentro(30)

carro2.velocimentro(30)

# Simulando o avanço do tempo e atualização das posições
rodovia1.atualizar_posicao_do_veiculo_na_rodovia(30)  # Atualiza as posições dos veículos baseado no tempo avançado (30 minutos)
rodovia2.atualizar_posicao_do_veiculo_na_rodovia(30) 
rodovia1.mostrar_veiculos()

rodovia2.mostrar_veiculos()

# 60 minutos intermediarios com velocidade constante de ...60...90...70
carro1.velocimentro(60)
caminhao1.velocimentro(90)
onibus1.velocimentro(100)

carro2.velocimentro(90)

rodovia1.atualizar_posicao_do_veiculo_na_rodovia(300)
rodovia1.mostrar_veiculos()

rodovia2.mostrar_veiculos()