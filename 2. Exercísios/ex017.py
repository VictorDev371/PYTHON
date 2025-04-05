print('DESASFIO 017')
print('')

from math import hypot
co= float(input('Qual é o cateto oposto: '))
ca= float(input('Qual é o cateto adjacente: '))
h= hypot(co, ca)
print('')

print('O valor da hipotenusa é {:.2}'.format(h))