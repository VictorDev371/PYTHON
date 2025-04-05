print('DESAFIO 012')

p = float(input('Qual a valor do produto: R$'))
po = int(input('Qual a porcentagem de desconto: '))
d = (p*po)/100
print('')

print('O novo preço do produto (R${}), será {:.2f}, com o desconto de {}%'.format(p, p-d, po))
print('')
