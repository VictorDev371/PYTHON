lista = []
totpar = []
valor09 = 0

for x in range(0,4):
    valores = int(input(f"Qual o {x}º valor?: "))
    lista.append(valores)
    if valores == 9:
        valor09 += 1
    elif valores % 2 == 0:
        totpar.append(valores)
lista = tuple(lista)

print(lista)
print(f"No total apareceram {valor09} vezes o valor 9")

if 3 in lista:
    print(f"O primeiro valor de 3 está na posição {lista.index(3)+1} da tupla")
else:
    print("O valor 3 não foi digitado")

print(f"No total esses foram os números pares {totpar}, caso esteja sem nada é porque não ouve")
