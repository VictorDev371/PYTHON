salario = float(input('Digite o valor do seu salario (coloque o "." para substituir "," de centavos e não use "." sem ser em centavos): R$'))

if salario >= 1250.00:
    print('Seu novo salario vai ser de R${:.2f}'.format((salario*10/100)+salario))
else:
    print('Seu novo salario vai ser de R${:.2f}'.format((salario*15/100)+salario))