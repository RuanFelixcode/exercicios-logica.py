matriz = []

lista1 = []

lista2 = []

for percoredor in range(3):
    n1 = int(input('digite um numero:'))
    lista1.append(n1)

matriz.append(lista1)

for percoredor1 in range(3):
    n2 = int(input('digite um numero:'))
    lista2.append(n2)
    
matriz.append(lista2)

cont = 0

for i in matriz:
    for percoredor2 in i :
        if percoredor2 % 2 == 0:
            cont +=1
            print(f'contagem de numeros pares {cont}')
