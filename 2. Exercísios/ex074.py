from random import randint
numeros = []

for x in range(5):
    sorteador = randint(0, 10)
    if x == 0:
        maior = menor = sorteador
    else:
        if sorteador > maior:
            maior = sorteador
        elif sorteador < menor:
            menor = sorteador
    numeros.append(sorteador)
numeros = tuple(numeros)
a, b, c, d, e = numeros

print(f"Os valores sorteados foram: {a, b, c, d, e}")
print(f"O menor valor sorteado foi {min(numeros)}")
print(f"O maior valor sorteador foi {max(numeros)}")
