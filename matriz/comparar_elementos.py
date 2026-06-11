matriz = []

lista1 = []

lista2 = []

for percoredor in range(2):
    n1 = int(input('digite um numero:'))
    lista1.append(n1)

matriz.append(lista1)

for percoredor1 in range(2):
    n2 = int(input('digite um numero:'))
    lista2.append(n2)
    
matriz.append(lista2)

for i in matriz:
    for percoredor2 in i :
        if percoredor2 > 10:
            print(f'numeros maiores que 10 -> {percoredor2}')
