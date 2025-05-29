total_gasto = 0
mais_de_mil = 0
produto_barato = float('inf')
nome_produto_barato = ''

while True:
    print('-'*30)

    nome_produto = str(input('Qual o nome do produto?: ')).strip().capitalize()
    valor_produto = float(input('Qual o valor do produto?: R$'))

    total_gasto += valor_produto

    if valor_produto > 1000:
        mais_de_mil += 1

    if valor_produto < produto_barato:
        produto_barato = valor_produto
        nome_produto_barato = nome_produto

    print('-'*30)

    resposta = str(input('Você quer continuar? [S/N]: ')).strip().upper()
    while resposta not in ['S', 'N']:
        resposta = str(input('Resposta inválida. Digite S ou N: ')).strip().upper()

    if resposta == 'N':
        print(f'''
Total gasto: R${total_gasto:.2f}
{mais_de_mil} produtos custam mais de R$1000
Produto mais barato: {nome_produto_barato} custando R${produto_barato:.2f}
''')
        break

    