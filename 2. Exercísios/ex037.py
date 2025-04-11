import math
n = int(input('Me informe o número inteiro: '))

print('- ESCOLHA COMO VOCÊ QUER CONVERTER -')
print('- "1" para binário')
print('- "2" para octal')
print('- "3" para hexadecimal')
resp = int(input('Respostas: '))

if resp == 1:
     print('Convertido para binario fica: {}'.format(bin(n)))
elif resp == 2:
     print('Convertido para binafio fica: {}'.format(oct(n)))
else:
     print('Convertido para hexadecimal fica: {}'.format(hex(n)))