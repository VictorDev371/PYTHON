print('DESAFIO 023')
print('')

numero= int(input('Me informe o número de 0 até 9999: '))
u= numero // 1 % 10
d= numero // 10 % 10
c= numero // 100 % 10
m= numero // 1000 % 10

print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))