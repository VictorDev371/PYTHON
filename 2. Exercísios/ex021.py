print('DESAFIO 021')
print('')

import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
input(pygame.event.wait())