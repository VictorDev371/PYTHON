peso_total = 0
peso_menor = 0

for c in range(5):
    peso = int(input('Qual o seu peso?: '))
    if c == 0:
        peso_total = peso_menor = peso
    else:
        if peso > peso_total:
            peso_total = peso
        if peso < peso_menor:
            peso_menor = peso

print(f'O maior peso foi de {peso_total}Kg e o menor peso foi de {peso_menor}Kg')

        
