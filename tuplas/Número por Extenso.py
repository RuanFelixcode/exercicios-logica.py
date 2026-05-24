'''Exercício Python 072: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quartoze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    opc = input('quer continuar s/n:')
    if opc == 'n':
        break
    n = int(input('digite um numero:'))
    if n < 0 or n > 20:
        print('numero invalido digite um numero entre 0 e 20')
        continue
    print(extenso[n])
