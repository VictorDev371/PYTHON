import datetime
ano_atual = datetime.date.today().year
ano_nasc = int(input('Ano de nascimento: '))

if ano_atual-ano_nasc == 18:
    print(f'Sua idade é de {ano_atual-ano_nasc} anos de idade, logo você DEVE se alistar no exercíto.')
elif ano_atual-ano_nasc < 18:
    print(f'Sua idade é de {ano_atual-ano_nasc} anos de idade, logo você não pode se alistar AINDA. Faltam {18-(ano_atual-ano_nasc)} anos para você se alistar.')
else:
    print(f'Sua idade é de {ano_atual-ano_nasc} anos de idade, logo você já PASSOU do tempo de se alistar no exercíto. Já se passou {(ano_atual-ano_nasc)-18} anos pós depois do tempo necessario do alistamento militar.')