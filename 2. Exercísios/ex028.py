from random import randint
from time import sleep
computador = randint(0, 5) # faz o computador sortear
print("-=-" * 10)
print('Em que um número entre 0 e 5.\n Tente adivinhar...')
print("-=-" * 10)
jogador = int(input("Em que número eu pensei? "))
print("PROCESSANDO...")
sleep(2)

if jogador == computador:
    print("PARABÉNS! Você conseguiu me vencer!")
else:
    print("GANHEI! Eu pensei no numero {} e não no {}".format(computador, jogador))




