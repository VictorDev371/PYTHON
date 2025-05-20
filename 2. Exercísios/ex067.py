while True:
    resposta = int(input('Tabuada de que número? '))
    if resposta < 0:
        break
    for x in range(1,11):
        print(f'{resposta} x {x} = {resposta*x}')
print('FIM!')