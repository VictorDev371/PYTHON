# if = se / vai ser o bloco verdadeiro
# else = senão / vai ser o bloco falso

nome= str(input('Qual é seu nome? '))
if nome== 'Gustavo':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')

print('Bom dia, {}'.format(nome))
print("")

#============ SEGUNDO EXEMPLO ===============

n1= float(input('Digite a primeira nota: '))
n2= float(input('Digite a segunda nota: '))
m= (n1+n2)/2
print('')

print('A sua média foi {:.1f}'.format(m))
if m>= 7:
    print('PARABÉNS! VOCÊ PASSOU')
else:
    print('Infelizmente você não obteve a pontuação.')