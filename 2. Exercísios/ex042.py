print("-=-" * 8)
print("ANALIZADOR DE TRIANGULO")
print("-=-" * 8)

r1 = float(input('Qual o valor da primeira reta? '))
r2 = float(input('Qual o valor da segunda reta? '))
r3 = float(input('Qual o valor da terceira reta? '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Vai ser possivel formar um triangulo')
    if r1 == r2 and r2 == r3:
        print('Esse triangulo é Equilátero')
    elif r1 == r2 != r3 or r2 == r3 != r1 or r3 == r1 != r2:
        print('Esse triangulo é Isósceles')
    elif r1 != r2 and r2 != r3 and r3 != r1:
        print('Esse triangulo é Escaleno')
else:
    print('Não vai ser possivel formar um triangulo, pois as 2 primeiras retas são menores que o valor da terceira')