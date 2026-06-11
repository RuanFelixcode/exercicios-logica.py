''' Numa eleição existem três candidatos. Faça um algoritmo que peça o número total de eleitores.
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.'''


qtd_eleitores = int(input('digite a quantidade de eleitores:'))
cont = 0
cont2 = 0
cont3 = 0
for i in range(1,qtd_eleitores+1):
    print('=-'*30)
    print(f'eleitor {i} vote no seu candidato')
    print(f'candidato1 quantidade de votos -> {cont}')
    print(f'eleitor {i} vote no seu candidato')
    print(f'candidato2 quantidade de votos -> {cont2}')
    print(f'eleitor {i} vote no seu candidato')
    print(f'candidato3 quantidade de votos -> {cont3}')
    print('=-'*30)
    votar = int(input('digite o numero de seu candidato:'))
    if votar == 1 :
        cont += 1
    elif votar == 2:
        cont2 += 1
    elif votar == 3:
        cont3 += 1
    else:
        print('cadidato nao exixte ')
        

    
        
        

    
    

