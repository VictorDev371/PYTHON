import time 

print('10 SEGUNDOS PARA OS FOGOS DE ARTIFICIOS!')
for c in range(10, -1, -1):
    print(f'{c}...')
    time.sleep(0.5)
print('*FOGOS EXPLODINDO*')
