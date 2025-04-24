from random import randint
from time import sleep

computador = randint(0, 5) # faz o computador sortear
print("-=-" * 10)
print('Em que um número entre 0 e 5.\n Tente adivinhar...')
print("-=-" * 10)
jogador = int(input("Em que número eu pensei? "))
print("PROCESSANDO...")

palpites = 0
while jogador != computador:
    print('Você errou :( , tente novamente!')
    jogador = int(input("Em que número eu pensei? "))
    palpites += 1

if jogador == computador:
    print(f"PARABÉNS! Você conseguiu me vencer!. Foram necessarios {palpites} para conseguir me vencer hehe")

