lista_idade = [0, 12, 14]
maiores_de_idades = []

def verificar_idade(idades=[]):
    for i in idades:
        if i >= 18:  
            maiores_de_idades.append(i)
    if not maiores_de_idades:
        return maiores_de_idades
    else:
        return maiores_de_idades

print(verificar_idade(lista_idade))
