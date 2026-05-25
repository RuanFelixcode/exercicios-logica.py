def maior (parametro):
    cont = 0
    maior = 0
    for i in parametro:
        if cont == 0:
            maior = i
            cont += 1
        if i > maior:
            maior = i
    return maior
lista = [1,23,4,5,5,6]
print(maior(lista))
