from time import sleep

velocidade= float(input('Qual a velocidade do carro (apenas o valor)? '))

print('PROCESSANDO...')
sleep(2)

if velocidade > 80:
    multa= (velocidade-80)*7
    print('Você ultrapassou a velocidade límite de 80km/h, por isso vai pagar uma multa de R${}'.format(multa))
else:
    print('Muito bem, sigua em frente na sua rota.')