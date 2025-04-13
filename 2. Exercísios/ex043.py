peso = float(input('Qual o seu peso: '))
altura = float(input('Qual a sua altura (em metros): '))
imc = peso/(altura**2)

if imc < 18.5:
    print(f'IMC = {imc:.1f}')
    print('Você está abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print(f'IMC = {imc:.1f}')
    print('Você está no peso ideal')
elif imc <= 30 and imc >=25:
    print(f'IMC = {imc:.1f}')
    print('Você está sobrepeso')
elif imc <= 40 and imc > 30:
    print(f'IMC = {imc:.1f}')
    print('Você está obeso')
else:
    print(f'IMC = {imc:.1f}')
    print('Você está em obesidade mórbida')