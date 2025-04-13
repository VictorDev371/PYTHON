import datetime
ano_atual = datetime.date.today().year
maioridade = 0
menoridade = 0

for c in range(7):
    ano_nasc = int(input('Qual a sua data de nascimento?: '))
    idade = ano_atual - ano_nasc
    if idade >= 21:
        maioridade += 1
    else:
        menoridade += 1
print(f'No total ainda faltam {menoridade} pessoas para atingir a maioridade, mas já tem {maioridade} pessoas de maiores')