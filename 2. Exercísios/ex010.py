print('DESAFIO 010')

real = float(input('Quanto de dinheiro você tem? R$'))
print('')

print('Você tem R${}, então você vai poder comprar U${:.2f}'.format(
    real, (real/3.27)))
print('')
