termo = int(input('Me informe o primeiro termo: '))
razao = int(input('Me informe a razão de PA: '))

for c in range(10):
    pa = termo+(c*razao)
    print(f'{c}º termo {pa}')
