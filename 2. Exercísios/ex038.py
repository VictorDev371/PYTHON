n1 = int(input('Me informe o primeiro número: '))
n2 = int(input('Me informe o segundo número: '))

if n1 > n2:
    print(f'O primeiro número, {n1}, é maior que o segundo.')
elif n2 > n1:
    print(f'O segundo número, {n2}, é maior que o primeiro.')
else:
    print(f'Ambos o primeiro {n1} e segundo {n2}, são iguais.')
