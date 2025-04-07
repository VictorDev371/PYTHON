nome = str(input('Qual é seu nome? '))

#CONDICIONAL ANINHADA -
if nome == 'Gustavo':
    print('Seu nome é tão comum')
elif nome == 'Pedro' or nome == 'Victor':
    print('Seu nome é incomum')
elif nome in 'Ana claúdia jessica juliana':
    print('Belo nome, lindo') 
else:
    print('Seu nome é bem comun')

print('tenha um bom dia {}!'.format(nome))