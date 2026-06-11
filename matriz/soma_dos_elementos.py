matriz = []
lista1 = []
lista2 = [] 
for i in range(2):
    n1 = int(input('digite um numero:'))
    lista1.append(n1)

matriz.append(lista1)
    
for x in range(2):
    n2 = int(input('digite um numero:'))
    lista2.append(n2)

matriz.append(lista2)

soma = 0
for percoredor in matriz:
    for somador in percoredor:
        print(f'''percorendo numeros...\nnumero atual: {somador} soma com o anterior {soma}''')
        soma += somador
print(f'resultado final da soma: {soma} ')  
    
