'''Um professor deseja analisar notas de alunos.
Crie um programa que:
• Leia notas até o usuário digitar -1
• Armazene em uma lista
• Mostre:
o Quantas notas são maiores ou iguais a 7
o Quantas são menores que 7'''
aprovados = []
reprovados = []
while True:
    nota = float(input('digite sua nota:'))
    if nota  == -1 :
        break 
    elif nota >= 7 and nota <= 10 :
        aprovados.append(nota)
    elif nota >= 1 and nota <= 6 :
        reprovados.append(nota)
    else:
        print('nota invalida')
print(f'lista de aprovados: {aprovados}')
print(f'lista de reprovados: {reprovados}')
        
