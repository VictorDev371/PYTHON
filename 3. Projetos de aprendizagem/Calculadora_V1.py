import time
import emoji

print('-=-=-=-=- CALCULADORA V2 -=-=-=-=-')
print('''
Escolha uma operação
 [➕ ] - 1 - Adição
 [➖ ] - 2 - Subtração
 [✖️  ] - 3 - Múltiplicação
 [➗ ] - 4 - Divisão
 OBS: Digite apenas o número informado
      ''')
quantidade = int(input('Quantidade totais de números: '))
resultado = 0
resultado_2 = 1
operacao = int(input('Qual a operação matemática: '))

if operacao in [1, 2, 3, 4]:
    for x in range(1, quantidade + 1):
        numero = float(input(f'{x}ª Número: '))
        if operacao == 1:
            resultado += numero
        elif operacao == 2:
            resultado = numero - resultado
        elif operacao == 3:
            resultado_2 *= numero
        else:
            resultado = resultado / numero
    print('Calculando...')
    time.sleep(2)
    if operacao == 3:
        print(f'O resultado foi {resultado_2}')
    else:
        print(f'O resultado foi {resultado}')
else:
    print('Você digitou algo errado, porfavor reinicie')