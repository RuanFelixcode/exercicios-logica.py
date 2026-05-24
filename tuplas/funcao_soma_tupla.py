def soma_tupla(*tupla):
    soma = 0
    for i in tupla :
        soma = i + soma
    return f'soma:{soma}'
print(soma_tupla(2,3,5)) 
