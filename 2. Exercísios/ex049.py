n = float(input('Me diga o número na qual você quer saber a tabuada: '))

print(f'-=-=-=-= TABUADA DE {n} =-=-=-=-')
for c in range(0, 11):
    print(f'{n} x {c} = {n*c}')