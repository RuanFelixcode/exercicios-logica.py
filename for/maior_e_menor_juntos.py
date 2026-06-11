menor = 0
maior = 0
cont = 0
lista = []
for i in range(5):
    n = int(input('digite um numero:'))
    lista.append(n)
for i in lista:
    if cont == 0:
        maior = i
        menor = i
        cont += 1
    if i > maior :
        maior = i
    if i < menor :
        menor = i
print(f'menor -> {menor}\nmaior -> {maior}')
