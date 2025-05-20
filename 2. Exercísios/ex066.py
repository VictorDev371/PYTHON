
soma = totn = 0

while True:
    n = int(input('Me diga um número [999 para parar]: '))
    if n == 999:
        break
    soma += n
    totn += 1

print(f'FIM!!!. A quantidade total de números foi de {totn} e a soma entre eles foi de {soma}')
