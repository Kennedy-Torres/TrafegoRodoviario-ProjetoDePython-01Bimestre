"""---"""
from print_cores import Cores

from modules.carro import Carro
from modules.onibus import Onibus
from modules.caminhao import Caminhao
from modules.estrada import Estrada


if __name__ == '__main__':
    
    fusca = Carro(
        placa='ABC-1234',
        modelo='Fusca',
        velocidade_maxima=120,
        velocidade_atual=60,
        #cidade_atual='São Paulo',
        #cidade_destino='Rio de Janeiro',
        faixa_atual=1,
        posicao=0
    )


    onibus = Onibus(
        placa='ABC-1234',
        modelo='Mini-Bus',
        velocidade_maxima=80,
        velocidade_atual=60,
        #cidade_atual='São Paulo',
        #cidade_destino='Rio de Janeiro',
        faixa_atual=2,
        posicao=0
    )
    
    caminhao = Caminhao(
        placa='PPO-5664',
        modelo='Volvo FH 540',
        velocidade_maxima=144,
        velocidade_atual=60,
        #cidade_atual='MG',
        #cidade_destino='RS',
        faixa_atual=2,
        posicao=0
    )
    
    estrada = Estrada(
        num_faixas=3,
        nome_da_estrada='Três corações',
        tamanho=300,
        cidade_inicial='São Paulo',
        cidade_final='Rio de Janeiro'        
    )
    
    estrada2 = Estrada(
        num_faixas=2,
        nome_da_estrada='Carvalho Velho',
        tamanho=440,
        cidade_inicial='MG',
        cidade_final='RS'        
    )
    
    # adicionando veículos à faixa inicial
    estrada.adicionar_veiculo(fusca, fusca.faixa)
    estrada.adicionar_veiculo(onibus, onibus.faixa)

    print(estrada)
    print("==============")

    ## Metodo para aumentar a velocidade, usando o metodo RANDOM
    while True:
        nova_velocidade = fusca.acelerar(fusca.vel_atual)
        print(f'-> {Cores.AZUL}Aumentando a velocidade de {fusca.vel_atual} KM/h para {nova_velocidade} KM/h durante 1hora{Cores.RESET}')
        if fusca.vel_atual < nova_velocidade < fusca.vel_maxima:
            fusca.vel_atual = nova_velocidade
            if estrada.verificar_fim_estrada(fusca):
                estrada.remov_veiculo(fusca)
                break
        else:
            print(f'{Cores.VERMELHO_CLARO}Velocidade acima da velocidade maxima do veiculo !{Cores.RESET}')
            fusca.vel_atual = fusca.vel_maxima
            break
    '''if estrada.verificar_fim_estrada(fusca):
        print("......CHEGOU........")
    else:
        print(".....Ainda não chegou.....")
    '''    
    print("=======================")
    fusca.mudar_de_faixa(estrada, 2)
    
    ## Metodo para reduzir a velocidade, usando o metodo RANDOM
    while True:
        nova_velocidade = fusca.desacelerar(fusca.vel_atual)
        print(f'-> {Cores.AZUL}Reduzindo a velocidade de {fusca.vel_atual} KM/h para {nova_velocidade} KM/h durante 1hora{Cores.RESET}')
        if nova_velocidade < fusca.vel_atual  and nova_velocidade>0:
            fusca.vel_atual = nova_velocidade
            if estrada.verificar_fim_estrada(fusca):
                estrada.remov_veiculo(fusca) 
                break
        else:
            fusca.vel_atual = 0
            print(f'{Cores.VERMELHO_CLARO}O veiculo está parado!{Cores.RESET}')
            break
    print("=======================")
    
    
    while True:
        nova_velocidade = onibus.acelerar(onibus.vel_atual)
        print(f'-> {Cores.AZUL}Aumentando a velocidade de {onibus.vel_atual} KM/h para {nova_velocidade} KM/h durante 1hora{Cores.RESET}')
        if onibus.vel_atual < nova_velocidade < onibus.vel_maxima:
            onibus.vel_atual = nova_velocidade
            if estrada.verificar_fim_estrada(onibus): 
                estrada.remov_veiculo(onibus)
                break
        else:
            print(f'{Cores.VERMELHO_CLARO}Velocidade acima da velocidade maxima do veiculo !{Cores.RESET}')
            onibus.vel_atual = onibus.vel_maxima
            break
    print("=======================")
    onibus.mudar_de_faixa(estrada, 1)
    
    while True:
        nova_velocidade = onibus.desacelerar(onibus.vel_atual)
        print(f'-> {Cores.AZUL}Reduzindo a velocidade de {onibus.vel_atual} KM/h para {nova_velocidade} KM/h durante 1hora{Cores.RESET}')
        if nova_velocidade < onibus.vel_atual  and nova_velocidade>0:
            onibus.vel_atual = nova_velocidade
            if estrada.verificar_fim_estrada(onibus):
                estrada.remov_veiculo(onibus) 
                break
        else:
            onibus.vel_atual = 0
            print(f'{Cores.VERMELHO_CLARO}O veiculo está parado!{Cores.RESET}')
            break
    print("=======================")
    
    print(estrada)
    print("=======================")
    
    estrada2.adicionar_veiculo(caminhao, caminhao.faixa)
    print(estrada2)
    print("=======================")
    
    while True:
        nova_velocidade = caminhao.acelerar(caminhao.vel_atual)
        print(f'-> {Cores.AZUL}Aumentando a velocidade de {caminhao.vel_atual} KM/h para {nova_velocidade} KM/h durante 1hora{Cores.RESET}')
        if caminhao.vel_atual < nova_velocidade < caminhao.vel_maxima:
            caminhao.vel_atual = nova_velocidade
            if estrada.verificar_fim_estrada(caminhao): 
                estrada.remov_veiculo(caminhao)
                break
        else:
            print(f'{Cores.VERMELHO_CLARO}Velocidade acima da velocidade maxima do veiculo !{Cores.RESET}')
            caminhao.vel_atual = caminhao.vel_maxima
            break
    print("=======================")
    caminhao.mudar_de_faixa(estrada2, 1)
    
    while True:
        nova_velocidade = caminhao.desacelerar(caminhao.vel_atual)
        print(f'-> {Cores.AZUL}Reduzindo a velocidade de {caminhao.vel_atual} KM/h para {nova_velocidade} KM/h durante 1hora{Cores.RESET}')
        if nova_velocidade < caminhao.vel_atual  and nova_velocidade>0:
            caminhao.vel_atual = nova_velocidade
            if estrada.verificar_fim_estrada(caminhao):
                estrada.remov_veiculo(caminhao) 
                break
        else:
            caminhao.vel_atual = 0
            print(f'{Cores.VERMELHO_CLARO}O veiculo está parado!{Cores.RESET}')
            break
    print("=======================")
    print(estrada2)