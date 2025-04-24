sexo = ['M', 'F']
resp = str(input('Qual é o seu Sexo?[M/F]  ')).upper()

while resp not in sexo:
    print('Tente novamente, porfavor.')
    resp = str(input('Qual é o seu Sexo?[M/F]  ')).upper()
print('Parabén, você digitou seu sexo corretamente!!')
