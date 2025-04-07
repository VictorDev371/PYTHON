n1 = int(input('Qual é o first number? '))
n2 = int(input('Qual é o second number? '))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print('')
print('A soma vai ser {}, \n o produto {} \n e a divisão vai ser {:.2f}'.format(s, m, d), end='')
print('Divisão inteira de {} \n e potência de {}'.format(di, e))
# \n = quebra de linha
# end='' = continuar os prints na mesma linha
# x**(1/2) = raiz quadrada de um número