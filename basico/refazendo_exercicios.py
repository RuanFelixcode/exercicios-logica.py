n1 = float(input('digite sua nota '))
n2 = float(input('digite sua nota '))
n3 = float(input('digite sua nota '))
media = (n1 + n2 + n3)/3
if media >=7:
    print(f'aprovado sua media foi {media:.2f}')
elif media == 6 or media == 5:
    print(f'recuperaçao sua nota foi {media:.2f}')
elif media <=4:
    print(f'reprovado sua media foi {media:.2f}')
