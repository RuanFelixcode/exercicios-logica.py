'''2. Campeonato de futebol
Um sistema registra a idade dos jogadores de um time:
• O usuário deve informar 10 idades
• Ignorar jogadores com idade 0 (dados inválidos)
• Mostrar:
o Quantos jogadores são maiores de idade
o Quantos são menores de idade'''
cont = 0
cont2 = 0
for i in range(10):
    idade = int(input('digite sua idade '))
    if idade <= 0 :
        continue
    elif idade >= 18:
        cont += 1
    elif idade < 18:
        cont2 += 1
    else:
        print('digite apenas a idade ')
print(f'o total de jogadores maiores de idade sao {cont} o total de jogadores menores de idade sao {cont2}')
        
