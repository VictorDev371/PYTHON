print('-- CAIXA ELETRONICO --')

nota50 = nota20 = nota10 = nota01 = valor_final = 0

valor = int(input('Qual valor você quer sacar? R$'))

while valor > 0: 
    if valor >= 50:
        valor -= 50
        nota50 += 1
    elif valor >= 20:
        valor -= 20
        nota20 += 1
    elif valor >= 10:
        valor -= 10
        nota10 += 1
    else:
        valor -= 1
        nota01 += 1

print(f'Total de {nota50} cédulas de R$50 \nTotal de {nota20} cédulas de R$20 \nTotal de {nota10} cédulas de R$10 \nTotal de {nota01} cédulas de R$1')
print('='*30)
print('Volte sempre ao BANCO, Tenha um bom dia!')
            