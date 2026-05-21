'''Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''

lista = []
while True:
    n = int(input('digite um valor:'))
    if n in lista:
        print('valor ja esta na lista')
    else:
        lista.append(n)
    opc = input('quer continuar s/n:')
    if opc == 'n':
        break
    elif opc == 's':
        continue
    else:
        print('valor invalido')
        
lista.sort()
print(lista)
