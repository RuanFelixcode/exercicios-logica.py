matriz = []

lista1 = []

lista2 = []

for percoredor1 in range(2):
    n1 = int(input('digite um numero:'))
    lista1.append(n1)

matriz.append(lista1)
   
for percoredor2 in range(2):
    n2 = int(input('digite um numero:'))
    lista2.append(n2)

matriz.append(lista2)

digitar = int(input('digite um numero:'))

for percoredor3 in matriz:
    for i in percoredor3:
        print(f'multiplicação\n{digitar} x {i} = {digitar*i}')

