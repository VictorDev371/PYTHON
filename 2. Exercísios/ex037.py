import math

n = int(input('Me informe o número inteiro: '))
print('''- ESCOLHA COMO VOCÊ QUER CONVERTER -')
- "1" para binário')
- "2" para octal')
- "3" para hexadecimal''')
resp = int(input('Respostas: '))

if resp == 1:
     print('Convertido para binario fica: {}'.format(bin(n)[2:]))
elif resp == 2:
     print('Convertido para octal fica: {}'.format(oct(n)[2:]))
elif resp == 3:
     print('Convertido para hexadecimal fica: {}'.format(hex(n)[2:]))
else:
     print('Numero digitado não corresponde a tabela')