'''
Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''
n1 = int(input('digite o primeiro valor '))
n2 = int(input('digite o segundo valor '))
print('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
opc = int(input('digite: '))
while opc != 5 :
    print('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
    if opc == 1:
        print(f'a soma entre {n1} + {n2} = {n1+n2}')
    elif opc == 2:
        print(f'a multiplicaçao entre {n1} x {n2} = {n1*n2}')
    elif opc == 3:
        if n1 > n2 :
            print('o primeiro valor e maior')
        else:
            print('o segundo e maio')
    elif opc == 4:
        print('digite novos valores ')
        n1 = int(input('digite o primeiro valor '))
        n2 = int(input('digite o segundo valor '))
    opc = int(input('digite a nova opçao: '))
print('programa finalizado')
