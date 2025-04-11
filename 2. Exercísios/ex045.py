print('-=-'*20)
print('JOKENPÔ - TENTE GANHAR DE MIM - HAHAHA')
print('-=-'*20)

import random
import time
lista = ["PAPEL!", "TESOURA!", "PEDRA!"]
maquina = random.choice(lista)
nome = str(input('Qual o seu nome, jogador(a): '))
print('''
    -=-=- TÁBELA DE ESCOLHAS -=-=-
      
      - Papel   - 
      - Tesoura -
      - Pedra   -

      Obs: Digite apenas o nome. ex: "Papel"
    -=-=-  FIM DAS ESCOLHAS  -=-=-
''')
jogador = str(input(f'Escolha sua jogada jogador(a) {nome} : '))
print('Eu escolhi...')
time.sleep(2)
print(maquina)

if maquina == 'PAPEL!' and jogador == 'Papel' or maquina == 'PEDRA!' and jogador == 'Pedra' or maquina == 'TESOURA!' and jogador == 'Tesoura':
    print('Putz... Deu empate... VAMOS OUTRA VEZ!')
elif maquina == 'PEDRA!' and jogador == 'Tesoura':
    print('HAHAHA, EU GANHEI!, TENTE NOVAMENTE PERDEDOR.')
elif maquina == 'PEDRA!' and jogador == 'Papel':
    print('Impossivel... Eu perdi... Como...')
    time.sleep(2)
    print(f'PARABÉNS JOGADOR {nome}')
elif maquina == 'PAPEL!' and jogador == 'Pedra':
    print('HAHAHA, EU GANHEI!, TENTE NOVAMENTE PERDEDOR.')
elif maquina == 'PAPEL!' and jogador == 'Tesoura':
    print('Impossivel... Eu perdi... Como...')
    time.sleep(2)
    print(f'PARABÉNS JOGADOR {nome}')
elif maquina == 'TESOURA!' and jogador == 'Papel':
    print('HAHAHA, EU GANHEI!, TENTE NOVAMENTE PERDEDOR.')
elif maquina == "TESOURA!" and jogador == 'Pedra':
    print('Impossivel... Eu perdi... Como...')
    time.sleep(2)
    print(f'PARABÉNS JOGADOR {nome}')