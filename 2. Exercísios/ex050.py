s = 0
quantidade = 0
for c in range(1, 7):
    n = float(input(f'{c}º número: '))
    if (n%2==0):
        s += n
        quantidade += 1
print(f'A soma dos valores pares resultou em {s}, e você me mostrou {quantidade} números.')