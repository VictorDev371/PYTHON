termo = int(input('Me informe o primeiro termo: '))
razao = int(input('Me informe a razão de PA: '))
c = 1
total = termo

while c <= termo:
    pa = termo + (c-1)*razao
    print(f'{c}º termo {pa}')
    c += 1

resposta = 'S'
lista = ['S', 'N']

while resposta == 'S':
    resposta = str(input('Você quer continuar?[S/N] ')).upper()
    if resposta in lista:
        if resposta == 'S':
         mais = int(input('Mais quantos termos você quer? '))
         total += mais
         while c <= total:
            pa = termo + (c-1)*razao
            print(f'{c}º termo {pa}')
            c += 1

        else:
           print('Fim do programa :)')
    else:
       print('Comando não esperado!!!. Porfavor me informe a correta')
       while resposta not in lista:
          resposta = str(input('Você quer tentar outra vez?[S/N] ')).upper()


