termo = int(input('Me informe o primeiro termo: '))
razao = int(input('Me informe a razão de PA: '))

c = 1
while c <= 10:
    pa = termo + (c-1)*razao
    print(f'{c}º termo {pa}')
    c += 1
