matriz = []

for i in range(3):
    lista = []
    for x in range(3):
        valor = int(input('digite um numero:'))
        lista.append(valor)
    matriz.append(lista)
    
print(f'matriz\n{matriz}')

for j in range(3):
    print(f'{matriz[j][j]}')
