palavras = ("ESTUDAR", "PROGRAMAR", "APRENDER")
Verificador = ["A", "E", "I", "O", "U"]

for x in range(0, len(palavras)):
    vogais = []
    for letra in palavras[x]:
        if letra in Verificador:
            vogais.append(letra)
    print(f"Na palavra {palavras[x]}, temos {vogais}")
