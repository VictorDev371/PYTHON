peso = float(input('Qual o seu peso: '))
altura = float(input('Qual a sua altura (em metros): '))
imc = peso/(altura*altura)

if imc < 18.5:
    print('Você está abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Você está no peso ideal')
elif imc <= 30 and imc >=25:
    print('Você está sobrepeso')
elif imc <= 40 and imc > 30:
    print('Você está obeso')
else:
    print('Você está em obesidade mórbida')