N1 = int(input('Me informe o primeiro numero: '))
N2 = int(input('Me informe o segundo numero: '))
N3 = int(input('Me informe o terceiro numero: '))


# - MAIOR -
if N1 > N2 and N1 > N3:
    print("{} é o maior número".format(N1))
else:
    if N2 > N1 and N2 > N3:
        print("{} é o maior número".format(N2))
    else:
        if N3 > N1 and N3 > N2:
            print("{} é o maior número".format(N3))

# - MENOR -
if N1 < N2 and N1 < N3:
    print("{} é o menor número".format(N1))
else:
    if N2 < N1 and N2 < N3:
        print("{} é o menor número".format(N2))
    else:
        if N3 < N1 and N3 < N2:
            print("{} é o menor número".format(N3))
