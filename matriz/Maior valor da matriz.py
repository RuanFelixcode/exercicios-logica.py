matriz = []

for i in range(3):
    lista = []
    for x in range(3):
        valor = int(input('digite um numero:'))
        lista.append(valor)
    matriz.append(lista)
    
print(f'matriz\n{matriz}')

maior = 0
for j in max(matriz):
    if j > maior:
        maior = j
print(maior)
