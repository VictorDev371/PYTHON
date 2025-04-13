#Inicio
print('-='*15)
print('    CALCULADORA MINIMALISTA ')
print('-='*15)

#meio
print(''' - Escolha uma opção -
[ 0 ] Múltiplicar
[ 1 ] Somar
[ 2 ] Dívidir
[ 3 ] Subtrair 
''')
lista = [0, 1, 2, 3]
n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
operacao = int(input('Escolha a operação: '))

#final
if operacao not in lista:
    print('Você digitou o valor errado, tente novamente')
else:
    if operacao == 0:
        print(f'{n1} x {n2} = {n1*n2:.2f}')
    elif operacao == 1:
        print(f'{n1} + {n2} = {n1+n2:.2f}')
    elif operacao == 2:
        print(f'{n1} / {n2} = {n1/n2:.2f}')
    elif n2 == 0:
        print('Não é possivel dividir o número por zero')
    else:
        print(f'{n1} - {n2} = {n1-n2:.2f}')
