'''Sistema de pedidos (lanchonete)
Funções obrigatórias:
• Exibir menu de produtos
• Permitir escolher itens
• Somar valor total
• Repetir pedidos até finalizar'''
soma = 0
while True:
    print('''menu de produtos
hamburge [1] 10:R$
batata frita [2] 5:R$
refrigerante [3] 4:R$
sair [4]''')
    opc = int(input('digite o numero do produto que quer: '))
    if opc == 1 :
        soma += 10
        print('pedido anotado hamburge')
    elif opc == 2 :
        soma += 5
        print('pedido anotado batata frita')
    elif opc == 3 :
        soma += 4
        print('pedido anotado refrigerante')
    elif opc == 4 :
        break
    else:
        print('digite uma opçao valida')
print(f'valor total:{soma}')
