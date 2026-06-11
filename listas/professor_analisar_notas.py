'''Um professor deseja analisar notas:
notas = [7.5, 8.0, 6.5, 9.0]
Mostre:
• menor nota
• maior nota
• média da turma'''
notas = [7.5, 8.0, 6.5, 9.0]
soma = 0
for i in notas:
    soma = i + soma
maior = max(notas)
menor = min(notas)
print(f'maior nota {maior} menor nota {menor} media {soma/len(notas)}')
    
