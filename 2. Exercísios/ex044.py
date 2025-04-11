produto = float(input('Qual o valor do produto? R$'))
print('[ 1 ] = à vista no dinheiro/cheque: 10 porcento de desconto')
print('[ 2 ] = à vista no cartão: 5 porcento de desconto')
print('[ 3 ] = em até 2x no cartão: preço normal')
print('[ 4 ] = 3x ou mais no cartão: 20 porcento de juros')
print('')
pagamento = int(input('Qual a forma de pagamentor? '))

if pagamento == 1:
    produto = produto-((produto*10)/100)
    print(f'À vista no dinheiro/cheque ficara R${produto:.2f} o produto.')
elif pagamento == 2:
    produto = produto-((produto*5)/100)
    print(f'À vista no cartão ficará R${produto:.2f}')
elif pagamento == 3:
    print(f'Em até 2x no cartão, o preço continuara sento R${produto:.2f}')
else:
    produto = ((produto*20)/100)+produto
    print(f'Em 3x ou mais no cartão, o preço ficará de R${produto:.2f}')
