#bibliotecas
import emoji
import random
import time

#introdução
print('\033[34m-=-\033[m'*15)
print('\033[34m       JOKENPÔ - TENTE GANHAR DE MIM\033[m')
print('\033[34m-=-\033[m'*15)
lista = ["PAPEL", "TESOURA", "PEDRA"]
validas = ["PAPEL", "TESOURA", "PEDRA"]
maquina = random.choice(lista)
print('\033[33mSEJA BEM VINDO! ao JOKENPÔ no Terminal\033[m')
nome = str(input('Qual o seu nome, jogador(a): '))

#meio
print(emoji.emojize('''
\033[34m-=-=-=-=- TÁBELA DE ESCOLHAS -=-=-=-=-\033[m\n
      - \033[37mPedra\033[m     [:rock:  ] 
      - Papel     [:newspaper: ]
      - \033[36mTesoura\033[m   [:scissors:  ] \n
      \033[35mObs: Digite apenas o nome.\033[m\n
\033[34m-=-=-=-=- FIM DAS ESCOLHAS  -=-=-=-=-\033[m
'''))

#meio fim 
jogador = input(f'\033[36mEscolha sua jogada , jogador(a) {nome} :\033[m ').strip().upper()
print(f'Sua jogada foi \033[33m{jogador}\033[m, vamos vêr a que eu escolhi...')
print('Jo...')
time.sleep(2)
print('Ken...')
time.sleep(1)
print('PÔ!')
print(f'\033[33m{maquina}\033[m')

#fim
if jogador not in validas:
    print('Você digitou algo errado que está fora da tabela, revise e tente novamente!')
else:
    if maquina == jogador:
        print('Infelizmente deu \033[31mempate\033[m :/ , vamos outra vez!')
    elif maquina != jogador:
        if (maquina == 'PEDRA' and jogador == 'TESOURA') or \
           (maquina == 'PAPEL' and jogador == 'PEDRA') or \
           (maquina == 'TESOURA' and jogador == 'PAPEL'):
            print('HA, eu ganhei, \033[31mtente novamente\033[m :>')
        else:
            print('Impossivel... \033[32mPARABÉNS\033[m JOGADOR :)')





