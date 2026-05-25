def vogais (texto):
    cont = 0
    for i in texto:
        if i.isalpha():
            cont +=1
    print(f'quantidade de vogais {cont}')
vogais('texto47') 
