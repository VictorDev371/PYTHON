from time import sleep

resp = 0
n1 = float(input('Valor do primeiro número: '))
n2 = float(input('Valor do segundo número: '))

while resp != 5:
    print(''' - TABELA -
    [1] Somar
    [2] Múltiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair do Programa
    ''')
    resp = float(input(f'Oque você deseja realizar com {n1} e {n2}?: '))

    if resp in [1, 2, 3, 4, 5]:
        if resp == 1:
            print(f'A soma de {n1} + {n2} dará: {n1+n2}')
        elif resp == 2:
            print(f'A multiplicação de {n1} x {n2} dará: {n1*n2}')
        elif resp == 3:
            if n1 > n2:
                print(f'{n1} é o maior valor')
            else:
                print(f'{n2} é o maior valor')
        elif resp == 4:
            print('Porfavor me informe os novos números')
            n1 = float(input('Valor do primeiro número: '))
            n2 = float(input('Valor do segundo número: '))
        else:
            print('Fim do programa ;D')
    else:
        print('Você digitou algum número fora dos que estão na lista, porfavor repita.')
    print('Processando...')
    sleep(1)

    