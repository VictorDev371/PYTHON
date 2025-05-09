n = int(input('Me informe o número: '))
n1 = 0
n2 = 1
n3 = 0

print('- SEQUENCIA DE FIBONACCI ABAIXO -')
print('0', end='')

c = 1
while c <= n-1:
    if c == 1:
        n3 = n1 + n2
        print(f' > {n3}', end='')
    else:
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        print(f' > {n3}', end='')
    c += 1