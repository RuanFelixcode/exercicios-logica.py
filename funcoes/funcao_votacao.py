def voto():
    ano_nascimento = int(input('digite seu ano de nascimento:'))
    ano_atual = 2026
    idade_aproximada = ano_atual - ano_nascimento
    if idade_aproximada == 16 or idade_aproximada == 17 :
        print('voto opcional')
    elif idade_aproximada < 16 :
        print('nao vota')
    elif idade_aproximada >=18 and idade_aproximada < 65:
        print('voto obrigatorio')
    elif idade_aproximada >= 65:
        print('voto opcional')
    return f'idade:{idade_aproximada}'   
print(voto())
