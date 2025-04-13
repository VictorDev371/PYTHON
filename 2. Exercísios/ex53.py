frase = str(input('Me diga a frase: '))
frase = frase.replace(" ", "").upper()
print(frase)

if frase == frase[::-1]:
    print(f'A frase é um palíndromo {frase[::-1]}')
else:
    print('Ela não é um palíndromo')