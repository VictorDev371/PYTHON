numero = int(input('Me informe o número: '))
divisores = 0

for c in range(1, numero+1): #se não colocar o +1 o código só vai pegar 1 número anterior ao do úsuario
    if numero % c == 0:
        divisores += 1
if divisores == 2:
    print('Ele é um número primo')
else:
    print('Ele não é um número primo')