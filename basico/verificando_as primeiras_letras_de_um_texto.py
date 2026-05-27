'''Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".'''

pergunta = input('em qual cidade voce nasceu?:').lower()
if 'santo' in pergunta:
    print(True)
else:
    print(False)
