print('DESAFIO 026')
print('')

nome= str(input('Me informe a frase que deseja: ')).strip().upper()  

print('A letra "A" aparece:', nome.count('A'),'vezes')
print('A palavra "A" aparece a primeira vez na parte: ', nome.find('A')+1)
print('A palavra "A" aparece na ultima vez na parte: ', nome.rfind('A')+1)