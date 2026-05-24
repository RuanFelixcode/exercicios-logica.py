'''
Exercício Python 004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
'''


a = input('digite ')
print(type(a))
print(a.isalpha)
print(a.isnumeric())
print(a.isspace())
print(a.isalnum())
print(a.isupper())
print(a.islower())
print(a.istitle())
