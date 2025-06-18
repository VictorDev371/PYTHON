produtos = ("Lápis", 1.75, "Boracha", 2.00, "Caderno", 15.90, "Estojo", 25.00, "Transferidor",
            4.20, "Compasso", 9.99, "Mochila", 120.32, "Canetas", 22.30, "Livros", 34.90)

print("-"*41)
print("          LISTAGEM DE PREÇOS")
print("-"*41)
for x in range(0, len(produtos), 2):
    nome = produtos[x]
    preço = produtos[x+1]
    print(f"{nome:.<30} R${preço:>7.2f}")
print("-"*41)
