import datetime
ano_nasc = int(input('Em que ano você nasceu? '))
ano_atual = datetime.date.today().year
idade = ano_atual - ano_nasc

if idade <= 9:
    print('Sua categoria é de MIRIM')
elif idade > 9 and idade <= 14:
    print('Sua categoria é de INFANTIL')
elif idade > 14 and idade <= 19:
    print('Sua categoria é de JUNIOR')
elif idade == 20:
    print('Sua categoria é de SÊNIOR')
else:
    print('SUA CATEOGIRA É MASTER!!!')