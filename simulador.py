"""---"""
from print_cores import Cores

from modules.carro import Carro
from modules.onibus import Onibus
from modules.estrada import Estrada


if __name__ == '__main__':
    
    # criando uma estrada com 3 faixas
    estrada = Estrada(3,"Tres corações")  
    
    fusca = Carro(
        placa='ABC-1234',
        modelo='Fusca',
        velocidade_maxima=120,
        velocidade_atual=60,
        cidade_atual='São Paulo',
        cidade_destino='Rio de Janeiro',
        faixa_atual=1,
        posicao=0
    )


    onibus = Onibus(
        placa='ABC-1234',
        modelo='Mini-Bus',
        velocidade_maxima=80,
        velocidade_atual=60,
        cidade_atual='São Paulo',
        cidade_destino='Rio de Janeiro',
        faixa_atual=2,
        posicao=0
    )
    
    # adicionando veículos à faixa inicial
    estrada.adicionar_veiculo(fusca, fusca.faixa)
    estrada.adicionar_veiculo(onibus, onibus.faixa)

    print(estrada)

    ## Metodo para aumentar a velocidade, usando o metodo RANDOM
    while True:
        nova_velocidade = fusca.acelerar(fusca.vel_atual)
        print(f'-> {Cores.AZUL}Aumentando a velocidade de {fusca.vel_atual} KM/h para {nova_velocidade} KM/h{Cores.RESET}')
        if fusca.vel_atual < nova_velocidade < fusca.vel_maxima:
            fusca.vel_atual = nova_velocidade
        else:
            print(f'{Cores.VERMELHO_CLARO}Velocidade acima da velocidade maxima do veiculo !{Cores.RESET}')
            fusca.vel_atual = fusca.vel_maxima
            break
    print("=======================")
    while True:
        nova_velocidade = onibus.acelerar(onibus.vel_atual)
        print(f'-> {Cores.AZUL}Aumentando a velocidade de {onibus.vel_atual} KM/h para {nova_velocidade} KM/h{Cores.RESET}')
        if onibus.vel_atual < nova_velocidade < onibus.vel_maxima:
            onibus.vel_atual = nova_velocidade
        else:
            print(f'{Cores.VERMELHO_CLARO}Velocidade acima da velocidade maxima do veiculo !{Cores.RESET}')
            onibus.vel_atual = onibus.vel_maxima
            break
    print("=======================")
        
    ## Metodo para reduzir a velocidade, usando o metodo RANDOM
    while True:
        nova_velocidade = fusca.desacelerar(fusca.vel_atual)
        print(f'-> {Cores.AZUL}Reduzindo a velocidade de {fusca.vel_atual} KM/h para {nova_velocidade} KM/h{Cores.RESET}')
        if nova_velocidade < fusca.vel_atual  and nova_velocidade>0:
            fusca.vel_atual = nova_velocidade
        else:
            fusca.vel_atual = 0
            print(f'{Cores.VERMELHO_CLARO}O veiculo está parado!{Cores.RESET}')
            break

    print("=======================")
    
    # Mudança de faixa
    fusca.mudar_de_faixa(estrada, 2)
    #onibus.mudar_de_faixa(estrada, 2)
    
    print(estrada)