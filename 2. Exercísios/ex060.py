from math import factorial

numero = int(input('Me informe o número do fatorial: '))
numero2 = numero
x = True
while numero2 != 1:
    if x:
        print(f'{numero2} ', end='')
        x = False
    else:
        numero2 -= 1
        print(f'x {numero2} ', end='')
print(f'= {factorial(numero)}', end='')
