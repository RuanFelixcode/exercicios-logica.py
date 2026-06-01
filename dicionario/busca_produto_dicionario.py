produtos = {}
while True:
    add = input('digite o nome do produto:')
    if add == 'fim':
        break
    preco = float(input('digite o preço:'))
    produtos.update({add:preco})
    
verificar = input('digite o nome do produto que deseja encontrar:')
if verificar in produtos:
    print('produto exite')
else:
    print('nao existe')
