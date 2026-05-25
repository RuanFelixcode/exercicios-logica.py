def cadastro():
    nome = input('digite seu nome:')
    senha = int(input('digite uma senha forte:'))
    validacao = int(input('confirme sua senha:'))
    if validacao != senha:
        while True:
            print('senha incorreta por favor confirme sua senha')
            validacao = int(input('confirme sua senha:'))
            if validacao == senha :
                break
    print('usuario registrado ')
cadastro()
