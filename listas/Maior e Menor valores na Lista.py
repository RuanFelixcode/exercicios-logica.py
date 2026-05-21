'''Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. '''
lista = [] 
maior = 0 
menor = 0
for i in range(5):
    n = int(input(f'digite um numero para a posição {i}:'))
    lista.append(n)
    
for x in lista:
    if x == 0 :
        maior = x
    elif x > maior :
        maior = x

for z in lista:
    if menor == 0 :
        menor = z
    elif z < menor :
        menor = z
        
print(f'''valores digitados {lista}\nmaior valor {maior} esta na posição {lista.index(maior)}\nmenor valor {menor} esta na posição {lista.index(menor)}''')
        
    
