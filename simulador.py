"""---"""
from modules.carro import Carro
from modules.onibus import Onibus


fusca = Carro(
    placa='ABC-1234',
    modelo='Fusca',
    velocidade_maxima=120,
    velocidade_atual=60,
    cidade_atual='São Paulo',
    cidade_destino='Rio de Janeiro')


onibus = Onibus(
    placa='ABC-1234',
    modelo='Mini-Bus',
    velocidade_maxima=80,
    velocidade_atual=60,
    cidade_atual='São Paulo',
    cidade_destino='Rio de Janeiro'
)

print(fusca.__dict__)
print(onibus.__dict__)
