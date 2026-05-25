login_simples():
    cont = 0
    while cont < 3:
        usuario = input('digite o nome de usuario:')
        senha = int(input('digite a senha:'))
        if usuario == 'admin' and senha == 123:
            print('bem vindo ao sistema')
            break
        else:
            cont +=1
            print('negado')
            
login_simples()
