# Criando o dicionário
produtos = {123: 'Camisa Estampada',
            124: 'Camisa social mana longa',
            125: 'Calça Jeans'}
print(produtos)

# Relacão de Vendas - Código do produto, QTD vendido e valor unitário
venda = [(122, 3 ,25.55), 
         (124, 2, 79.99),
         (125, 1, 99.99)]
print(venda)

# Função cupom fiscal

item = 0
valor_total = 0
print("-" * 46) # Imprime 46 vezes o caracter "-"
print('C U P O M  F I S C A L'.center(46, ' '))
print("ITEM CÓDIGO DESCRIÇÃO QTD.UN.VL_UNIT(R$) ST VL")
print("-" * 46)

for indice in range(0, len(venda)):
    subtotal = 0
    item += 1
    produto = produtos.get(venda[indice][0])
    quantidade = venda[indice][1]
    valor = venda[indice][2]
    subtotal += quantidade * valor
    valor_total += subtotal

    print(f'{str(item).ljust(4)}, {venda[indice][0]},{produto.rjust(37)}')
    print(f'{str(quantidade).rjust(11)} UN X,{str(valor).ljust(6)}, {str(subtotal).rjust(23)}')
    
    print("-" * 46)
    print('TOTAL R$', str(valor_total).rjust(37))