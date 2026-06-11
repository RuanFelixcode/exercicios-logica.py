'''
Crie um algoritmo que:
Leia uma matriz 3x3
Mostre a soma da primeira
coluna'''

matriz = []
lista1 = []
lista2 = [] 
lista3 = []
for i in range(2):
    n1 = int(input('digite um numero:'))
    lista1.append(n1)

matriz.append(lista1)
    
for x in range(2):
    n2 = int(input('digite um numero:'))
    lista2.append(n2)

matriz.append(lista2)

for j in range(2):
    n3 = int(input('digite um numero:'))
    lista3.append(n3)

matriz.append(lista3)

print(f'matriz\n{matriz}')

soma = sum(matriz[0])
print(f'soma da primeira coluna {soma}')
