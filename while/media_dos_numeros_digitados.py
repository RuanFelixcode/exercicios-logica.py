cont = 0 
soma = 0
while True:
    n = int(input('digite um numero:'))
    if n == 0:
        print('nao se da pra fazer media com 0')
        break
    soma = n + soma
    cont += 1
print(f'media {soma/cont:.2f}')
