'''Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
'''

while True:
    escolha = input('quer continuar s/n:')
    if escolha == 'n':
        break
    elif escolha != 's':
        print('selecione uma opçao valida')
        continue
    numero = float(input('digite um numero:'))
    if numero % 1 == 0 :
        print(f'numero inteiro -> {numero}')
    else:
        print(f'numero decimal -> {numero}')
