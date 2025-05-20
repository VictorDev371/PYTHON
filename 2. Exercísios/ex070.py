total_gasto = mais_de_mil = produto_barato = 0
primeira_volta = True

while True:
    print('-'*30)

    if primeira_volta:
        nome_produto = str(input('Qual o nome do produto?: ')).strip().capitalize()
    
        valor_produto = float(input('Qual o valor do produto?: '))
        total_gasto += valor_produto
        produto_barato += total_gasto
        if valor_produto > 1000:
            mais_de_mil += 1
        
        print('-'*30)

        resposta = str(input('Você quer continuar?: ')).strip().upper()
        while resposta not in ['S', 'N']:
            resposta = str(input('Você quer continuar?: ')).strip().upper()

        if resposta == 'N':
            print(f'O total gasto: R${total_gasto} \n {mais_de_mil} produtos custam mais de R$1000 \n O produto mais barato: {nome_produto_barato} custando R${produto_barato}')
            break
        primeira_volta = False
    else:
        nome_produto = str(input('Qual o nome do produto?: ')).strip().capitalize()
    
        valor_produto = float(input('Qual o valor do produto?: '))
        total_gasto += valor_produto
        if valor_produto > 1000:
            mais_de_mil += 1
        elif valor_produto < produto_barato:
            produto_barato = valor_produto
            nome_produto_barato = nome_produto
        
        print('-'*30)

        resposta = str(input('Você quer continuar?: ')).strip().upper()
        while resposta not in ['S', 'N']:
            resposta = str(input('Você quer continuar?: ')).strip().upper()

        if resposta == 'N':
            print(f'O total gasto: R${total_gasto} \n {mais_de_mil} produtos custam mais de R$1000 \n O produto mais barato: {nome_produto_barato} custando R${produto_barato}')
            break
        primeira_volta = False
    