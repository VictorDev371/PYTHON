print('DESAFIO 020')
print('')

from random import shuffle
a1 = str(input('Qual o nome do primeiro grupo?: '))
a2 = str(input('Qual o nome do segundo grupo?: '))
a3 = str(input('Qual o nome do terceiro grupo?: '))
a4 = str(input('Qual o nome do quarto grupo?: '))
lista = [a1, a2, a3, a4]
shuffle(lista)


print("ordem de apresentação será \n{}".format(lista))

