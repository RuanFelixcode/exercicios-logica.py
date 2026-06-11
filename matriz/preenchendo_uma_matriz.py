'''Crie um algoritmo que:
Leia valores para uma matriz
2x8
Mostre a matriz na tela'''

matriz = []
list1 = []
list2 = []
for i in range(8):
    n = int(input('digite um numero:'))
    list1.append(n)
for x in range(8):
    n2 = int(input('digite um numero:'))
    list2.append(n2)
matriz.append(list1)
matriz.append(list2)
for m in matriz:
    print(m)
