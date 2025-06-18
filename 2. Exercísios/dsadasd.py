frase = str(input("Me diga qual a frase: ")).split()
tot = 0
for x in frase:
    if len(x) >= 3:
        tot += 1
print(f"Total de palavras com 3 letras ou mais: {tot}")

