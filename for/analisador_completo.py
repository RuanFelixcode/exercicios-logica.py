'''Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''
nome_mais_velho = ''
idade_mais_velho = 0
mulheres_novas = 0
media_idades = 0
for i in range(1,5):
    print(f'------ pessoa:{i} ------')
    nome = input('digite seu nome:').strip()
    sexo = input('sexo (m/f):').strip().lower()
    idade = int(input('digite sua idade:').strip())
    media_idades += idade
    if sexo == 'm':
        if idade > idade_mais_velho:
            nome_mais_velho = nome
            idade_mais_velho = idade
    if sexo == 'f':
        if idade < 20:
            mulheres_novas += 1
            
print(f'media das idades: {media_idades/4}')
print(f'total de mulheres com menos de 20 -> {mulheres_novas} anos')
print(f'homem mais velho do grupo nome:{nome_mais_velho} idade: {idade_mais_velho}')
    
    
    
