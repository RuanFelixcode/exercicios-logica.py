'''Exercício Python 066: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).'''
soma = 0
cont = 0
while True:
    numero = int(input('digite um numero pra parar (999):').strip())
    if numero == 999:
        break
    soma += numero
    
print(f'a soma dos {cont} valores e {soma}')
