
maiores_de_18 = homens = mulheres_menos_20 = 0

while True:
    print('=='*20)

    idade = int(input('Qual a idade da pessoa?: '))

    if idade > 18:
        maiores_de_18 += 1

    sexo = str(input('Qual o sexo?[F/M]: ')).strip().upper()
    while sexo not in ['F', 'M']:
        sexo = str(input('Comando inesperado, qual o sexo?[F/M]: ')).strip().upper()

    if sexo == 'M':
        homens += 1
    elif sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1

    print('=='*20)

    option = str(input('Você quer continuar?[S/N]: ')).strip().upper()
    while option not in ['S', 'N']:
        option = str(input('Comando inesperado, você quer continuar?[S/N]: ')).strip().upper()

    if option == 'N':
        print(f'{maiores_de_18} pessoas maiores de 18, {homens} homens cadastrados, {mulheres_menos_20} mulheres que tem menos que 20 anos')
        break