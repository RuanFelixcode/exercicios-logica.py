'''9.
Uma escola deseja separar alunos por situação:
notas = []
Crie um programa que:
• Leia 5 notas
• Armazene na lista
• Percorra a lista e:
o Mostre "Aprovado" se nota >= 7
o Mostre "Recuperação" se nota entre 5 e 6.9
o Mostre "Reprovado" se nota < 5'''
notas = []
for i in range(5):
    n = float(input('digite sua nota:'))
    notas.append(n)
    
for i in notas:
    if i >= 7 and i <= 10: 
        print(f'nota {i} aprovado')
    elif  i == 5 or i > 5 :
        print(f'nota {i} recuperaçao')
    elif i < 5 and i > 0 :
        print(f'nota {i} reprovado')
    else:
        print(f'nota {i} invalida')
    
