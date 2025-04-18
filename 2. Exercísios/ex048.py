s = 0
n = 0
for c in range(1, 501, 2):
    if (c%3==0):
        s += c
        n += 1
print(f'O resultado foi de {s}')
print(f'Foram solicitados {n}')