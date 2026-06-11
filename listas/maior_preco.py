'''6.
Uma loja quer analisar vendas do dia:
vendas = [100, 250, 80, 300, 150, 30]
Crie um programa que:
• Percorra a lista
• Some apenas as vendas acima de 100
• Mostre o total '''
vendas = [100, 250, 80, 300, 150, 30] 
soma = 0 
for i in vendas :
    if i > 100:
        soma = soma + i 
print(soma)


