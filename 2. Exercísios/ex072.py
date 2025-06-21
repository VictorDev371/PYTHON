numeros = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte" )

usuario = int(input("Digite um número entre 0 e 20: "))
while usuario not in (range(21)):
     usuario = int(input("Tente novamente. Digite um número entre 0 e 20: "))
print(f'O número foi de {usuario}, por extenso ficará {numeros[usuario]}')

while True:
     pergunta = str(input("Você quer continuar?[S/N]")).upper().lstrip()
     if pergunta == "S":
          usuario = int(input("Digite um número entre 0 e 20: "))
          while usuario not in (range(21)):
               usuario = int(input("Tente novamente. Digite um número entre 0 e 20: "))
          print(f'O número foi de {usuario}, por extenso ficará {numeros[usuario]}') 
     elif pergunta == "N":
          break
     else:
          print('Porfavor tente novamente')