quantidade_de_numeros = c = somando_c = 0

while c != 999:
    c = int(input('Qual o valor do número?: '))
    if c != 999:
        somando_c += c
        quantidade_de_numeros += 1
print(f'Você digitou "999", logo o programa foi incerrado, o  resultado final: {quantidade_de_numeros} números digitados (desconsiderando "999"), e a soma entre eles foi de {somando_c}')