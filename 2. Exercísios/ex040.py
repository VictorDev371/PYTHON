n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
media = (n1+n2)/2

if media < 5:
    print(f'Infelizmente o aluno foi reprovado com media {media}, #triste')
elif 7 > media >= 5:
    print(f'O aluno deverá ir para a recuperação com media {media:.1f}, #ansiedade')
else:
    print(f'ALUNO FOI APROVADO COM SUCESSO COM MEDIA DE {media:.1f}!!!, #superfeliz')