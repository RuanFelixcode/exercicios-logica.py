'''10.
Uma loja quer analisar comportamento de clientes.
Crie um programa que:
• Leia o valor de compras de vários clientes (até digitar 0)
• Armazene em uma lista
• Depois:
o Mostre o maior valor
o Mostre o menor valor
o Mostre a média
o Mostre quantos clientes gastaram acima da média
'''
lista = []
soma = 0
while True:
    prt = float(input('digite o valor:'))
    if prt == 0:
        break
    lista.append(prt)

for i in lista:
    soma = soma + i
    
media = soma / len(lista)
print(f'media {media}')
print(max(lista))
print(min(lista))
for i in lista :
    if i > media:
        print(f'acima da media {i}')

