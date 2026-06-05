def notas(*varias_notas):
    total = len(varias_notas)
    media = sum(varias_notas)/len(varias_notas)
    maior = max(varias_notas)
    menor = min(varias_notas)
    alunos = {
        'total':total,
        'media': media,
        'maior':maior,
        'menor':menor,
    }
    
    if alunos['media'] >=10 and alunos['maior'] >=7 and alunos['menor']>= 5:
        alunos.update({'situação':'boa'})
        print(alunos)
    else:
        alunos.update({'situação':'ruim'})
        print(alunos)
