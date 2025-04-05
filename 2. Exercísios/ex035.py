print("-=-" * 8)
print("ANALIZADOR DE TRIANGULO")
print("-=-" * 8)

r1 = float(input('Qual o valor da primeira reta? '))
r2 = float(input('Qual o valor da segunda reta? '))
r3 = float(input('Qual o valor da terceira reta? '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Vai ser possivel formar um triangulo')
else:
    print('Não vai ser possivel formar um triangulo, pois as 2 primeiras retas são menores que o valor da terceira')