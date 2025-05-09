resposta = 'S'
lista = ['S', 'N']
ciclo = True
media = total = maior_numero = menor_valor = 0

while resposta == 'S':
    if ciclo == True:
        numero = int(input('Me informe o número: '))
        media = numero
        total = 1
        ciclo = False
        maior_numero = numero
        menor_valor = numero
    else:
        resposta = str(input('Você quer continuar?[S/N]')).upper()
        if resposta in lista:
            if resposta == 'S':
                numero = int(input('Me informe o número: '))
                media += numero
                total += 1
                if numero > maior_numero:
                    maior_numero = numero
                elif numero < menor_valor:
                    menor_valor = numero
            else:
                print('Fim do Programa :D')
        else:
            print('Parece que você digitou algo errado, vamos tentar novamente!')

tot_media = media/total
print(f'No fim, a media total dos números foi de {tot_media:.1f}, e o maior número foi {maior_numero} e o menor valor foi de {menor_valor}')