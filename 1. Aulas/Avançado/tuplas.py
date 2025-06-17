lanche = ('sorvete', 'suco', 'pudim')
#Tuplas só se usa "()"

for x in range(0, len(lanche)):
    print(lanche[x])
    #Precisa de posição

for x in lanche:
    print(f'Eu vou comer {x}')
    #Não precisar de posição

print(sorted(lanche))
#Maneira organizada, em ordem
