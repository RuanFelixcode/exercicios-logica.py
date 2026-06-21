def nome_com_aspas():
    while True:
        true_false = False
        nome = input('digite seu nome:').strip()
        if ' '  in nome:
            true_false = True
            nome_final = nome
        if not nome.replace(' ','').isalpha():
            print('so e permitido nomes simples ou compostos')
            continue
        return  nome_final
        
        
print(nome_com_aspas())
