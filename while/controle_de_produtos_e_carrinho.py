produtos = {"Salgado": 5.00, "Suco": 4.00, "Refrigerante": 6.00}
carrinho = []
while True:
    print('''1 - Mostrar produtos
2 - Comprar
3 - Adicionar produto
4 - Remover produto
5 - Mostrar total
0 - Sair''')
    opc = int(input('selecione uma opçao:'))
    #mostrar produtos e preços
    if opc == 1:
        for prod,preco in produtos.items():
            print(f"{prod}: {preco}")
        while True:
            
            item = input("Digite o nome do item: (0 para Sair)")
            if item == "0":
                print("Sistema encerrado!")
                break
            if item in produtos:
                print(f"{item} disponível!")
                print(f"R$ {produtos.get(item)}")
            else:
                print("Produto não existe na cantina!")
    elif opc == 2 :
        compras = input('digite o que deseja comprar:')
        if compras in produtos:
            carrinho.append(compras)
        else:
            print('produto nao existe')
    
    
    elif opc == 3:
        resposta=input("Deseja adicionar itens ao cardápio?(Digite s para Sim e n para Não)").lower()
        if resposta == 's':
        
            #Inserindo itens no dicionário
            qtd_add_produto = int(input("Quantos produtos deseja adicionar?")) 
            for i in range(qtd_add_produto): 
                novo_produto = input("Digite o nome do item:")
                valor_produto = float(input("Digite o preço do item:"))
                produtos.update({novo_produto: valor_produto})
    
    elif opc == 4 :
        resposta=input("Deseja remover itens do cardápio?(Digite s para Sim e n para Não)").lower()
        if resposta == 's':
            print(produtos)
            qtd_add_produto = int(input("Quantos produtos deseja remover?"))
            if len(produtos) < qtd_add_produto:
                print("Inválido")
            else:
                for i in range(qtd_add_produto): 
                    remove_produto = input("Digite o nome do item:")
                    produtos.pop(remove_produto)
    elif opc == 5:
        print(f"Quantidade de produtos disponíveis: {len(produtos)}")
        for a in produtos:
            print(a)
    elif opc == 0:
        print("Sistema encerrado!")
        break
    
    else:
        print('selecione uma opçao valida')

