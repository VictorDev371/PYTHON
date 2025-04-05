print('DESAFIO 016')
print('')

from math import radians, sin, cos, tan
angulo= float(input('Me informe o angulo: '))
sen= sin(radians(angulo))
cos= cos(radians(angulo))
tang= tan(radians(angulo))
print('')

print('O seno, cosseno e tangente do angulo de {}° é:\n Seno: {:.2f} \n Cosseno: {:.2f} \n Tangente: {:.2f}'.format(angulo, sen, cos, tang))
