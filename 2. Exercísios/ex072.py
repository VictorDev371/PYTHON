numeros = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte" )
numeros2 = (range(21))
usuario = int(input("Digite um número entre 0 e 20: "))

while usuario not in numeros2:
     usuario = int(input("Tente novamente. Digite um número entre 0 e 20: "))

print(f'O número foi de {usuario}, por extenso ficará {numeros[usuario]}')

