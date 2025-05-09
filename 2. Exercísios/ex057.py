sexo = ['M', 'F']
resp = str(input('Qual é o seu Sexo?[M/F]  ')).strip().upper()[0]

while resp not in sexo:
    print('Tente novamente, porfavor.')
    resp = str(input('Qual é o seu Sexo?[M/F]  ')).strip().upper()[0]
print('Parabén, você digitou seu sexo corretamente!!')
