frase= print('Curso em video python')
#Fatiamento de string, ex:
 #frase[9] = ele vai pegar o caracter nove (V)
 #frase[9:13] = ele vai do caractere 9 até 12 (Vide)
 #frase[9:21:2] = começar no 9 até 20 pulando de 2 (Vdo Pto)

#Analise de string, ex:
 #len(frase) = comprimento, a frase tem 21 caracteres de 0 até 21
 #frase.count('o') = contar quantas vezes aparece (3x)
  #frase.count('o', 0, 13) = contagem até o 12 (1x)
 #frase.find('deo') = quantas vezes encontrou (encontrado na 11)
 #'Curso' in frase = dentro da frase tem a palavra? (true)
 
#Transformação, ex:
 #frase.replace('Python', 'Android') = substituir
 #frase.upper() = colocar letras em maiusculo
 #frase.lower() = colocar letras em minusculo
 #frase.capitalize() = jogar toda a string em minúsculo menos a primeira
 #frase.title() = pós os espaços as letras ficam maiúsculas
 #frase.strip() = remover espaços inuteis do inicio e fim
  #frase.rstrip () = remover só a righ no final
  #frase.lstrip () = remover só a left no inicio

#Divisão
 #frase.split() = tirar os espaços, com novas listas
#Junção
 #'-'.joing(frase) = juntar as listas separadas mas colocando o sinal ao invez do espaço.