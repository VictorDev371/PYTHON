valor_casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Salario do comprador: R$'))
Anos = int(input('Em quantos anos você vai pagar : '))
Anos = Anos * 12
prest = valor_casa/Anos 
porcentagem = (salario*30)/100

print('O valor da sua casa R${}, ficara com o respectivo valor R${:.2f}, sendo parcelada em {} meses'.format(valor_casa, prest, Anos))

if prest >= porcentagem:
    print('Você não foi aprovado para o emprestimo')
else:
    print('Você foi aprovado para o emprestimo')