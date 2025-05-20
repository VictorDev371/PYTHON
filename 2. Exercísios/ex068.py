from random import randint

print('VAMOS JOGAR PAR OU ÍMPAR')

soma_resultado = ''
totv = 0

while True:
    humano = int(input('Digite um valor: '))
    par_ou_inpar = str(input('Par ou ímpar? [P/I] ')).upper()
    computador = randint(1, 10)
    soma = humano + computador

    if soma%2==0:
        soma_resultado = 'PAR'
    else:
        soma_resultado = 'IMPAR'

    if par_ou_inpar == 'P':
        par_ou_inpar = 'PAR'
    elif par_ou_inpar == 'I':
        par_ou_inpar = 'IMPAR'
    else:
        print('Você digitou algo errado')
        break

    print('--'*20)
    print(f'Você jogou {humano} e o computador {computador}. Total de {soma} DEU {soma_resultado}')
    print('--'*20)
    
    if par_ou_inpar == soma_resultado:
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        totv += 1
    else:
        print(f'GAME OVER! Você venceu {totv} vezes.')
        break
