#import math ( todas as funcionalidades do modulo)
#from math import sqrt ( apenas algo)

# - BÍBLIOTECA MATH -
#Arredondar para cima ( ceil )
#Arredondamento para baixo ( floor )
#Eliminar da vírgula para frente ( trunc )
#Calcular raiz quadrada ( sqrt )
#Calculo fatorial ( factorial )

import math
num= int(input('Digite um número: '))
raiz= math.sqrt(num)
print('')

print('A raiz de {} é igual a {}'.format(num, math.floor(raiz)))
