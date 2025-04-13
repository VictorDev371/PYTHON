Total_par = 0
for c in range(1,51):
    if c%2==0:
        print(f'{c} é um número par')
        Total_par += 1
print(f'FIM, o total de número pares foi de {Total_par}')