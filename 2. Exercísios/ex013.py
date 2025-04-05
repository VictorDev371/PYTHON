print('DESAFIO 013')

s= float(input('Qual o valor do salario? R$'))
p= int(input('Qual é a porcentagem de aumento (desconsidere a porcentagem)? '))
print('')

print('O novo salário do escravo vai ser de R${:.2f} com o aumento de {}%'.format(s+((s*p)/100), p))
print('')