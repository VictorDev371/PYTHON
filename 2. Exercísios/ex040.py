n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
media = (n1+n2)/2

if media < 5:
    print('Infelizmente o aluno foi reprovado, #triste')
elif media >= 5 and media <= 6.9:
    print('O aluno deverá ir para a recuperação, #ansiedade')
else:
    print('ALUNO FOI APROVADO COM SUCESSO!!!, #superfeliz')