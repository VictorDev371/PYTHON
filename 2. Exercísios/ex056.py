maior_idade = 0
mulheres = 0
maior_idade_nome = "[Sem Homem]"
media = 0
pessoas = int(input('Quantas pessoas existem? '))

for pessoa in range(1, pessoas+1):
    nome = str(input(f'Qual o nome da {pessoa}º pessoa? '))
    idade = int(input(f'Qual a idade da {pessoa}º pessoa? '))
    sexo = str(input(f'Qual o sexo da {pessoa}º pessoa?[M/F] ')).upper()
    sexo = sexo.replace(" ", "")
    #Algoritmo para saber o homem mais velho
    if sexo == "M":
        if pessoa == 1:
            maior_idade = idade
            maior_idade_nome = nome
        elif idade > maior_idade:
            maior_idade_nome = nome
            maior_idade = idade
    #Algoritmo para saber quantas mulheres tem 20 anos
    elif sexo == "F":
        if idade < 20:
            mulheres += 1
    #Algoritmo para saber a media do grupo
    media += idade

print(f'O homem mais velho foi: {maior_idade_nome} com a idade de {maior_idade}')
print(f'Existem cerca de {mulheres} mulheres menores de vinte anos')
print(f'A media das pessoas foram de {media/pessoas}')


    

