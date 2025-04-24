numero = int(input('Me informe o número do fatorial: '))
multiplicador = numero-1
resultado = 0

while multiplicador != 0:
    if multiplicador == numero-1:
        resultado = numero * multiplicador
    else:
        multiplicador -= 1
        tot = resultado * multiplicador
    print(f'{resultado}')
print(f'O resultado final foi de:{tot}')