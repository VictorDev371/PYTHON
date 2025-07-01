lista = []

for x in range(1, 6):
    number = int(input(f'Digite o {x}ª valor: '))
    lista.append(number)
print(lista)

print(
    f"Maior valor digitado foi {max(lista)}, na posição {lista.index(max(lista))}... {lista.index(max(lista))+1}")


print(
    f"Menor valor digitado foi {min(lista)}, na posição {lista.index(min(lista))}")

#FALTA TERMINAR!!!
