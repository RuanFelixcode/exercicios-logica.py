'''Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''
idade_mais_velho = 0
media_idade = 0
cont = 0
for i in range(1,5):
    print(f'------ PESSOA {i} ------')
    nome = input('digite seu nome:')
    idade = int(input('digite sua idade:'))
    sexo = input('digite seu sexo (m/f):')
    if idade >= media_idade:
        media_idade+= idade
        
    if sexo == 'm':
        if idade > idade_mais_velho:
            mais_velho = nome
            idade_mais_velho = idade
    if sexo == 'f':
        if idade < 20:
            cont+= 1

print(f'media das idade {media_idade/4}')
print(f'o homem mais velho se chama {mais_velho} com {idade_mais_velho} anos')
print(f'total de mulheres com menos de 20 -> {cont}')
