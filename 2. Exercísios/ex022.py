print('DESAFIO 022')
print('')

nome = input('Qual o seu nome: ')
Snome = nome.strip()
Snome2= Snome.replace(' ', '')
print('')
print('O seu nome, "{}", pode ficar da seguinte forma:\n Todas as letras Maiúsculas: {} \nTodas as letras minúsculas: {} \nTodas as letras ao todo: {} \nQuantas letras tem o primeiro nome: {}'.format(nome, nome.upper(), nome.lower(), len(Snome2), len(nome.split()[0])))
print('')
