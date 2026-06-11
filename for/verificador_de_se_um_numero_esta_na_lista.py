lista = []
for i in range(5):
    n = int(input('digite um numero:'))
    lista.append(n)
verificar = int(input('verifique se o numero esta na lista:'))
if verificar in lista:
    print(f'o numero {verificar} esta na lista')
else:
    print(f'o numero {verificar} nao esta na lista')
    
