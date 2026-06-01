'''Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
'''
def registrar_nome():
    while True:
        nome = input('digite seu nome:')
        if not nome.replace(' ','').isalpha():
            print('so e permitido nomes simples ou compostos')
            continue
        return nome
        
def registrar_sexo():
    while True:
        sexo = input('sexo (m/f):')
        if sexo == 'm':
            return sexo
        elif sexo == 'f':
            return sexo
        else:
            print('sexo invalido')
            
def registrar_idade():
    while True:
        try:
            idade = int(input('digite sua idade:'))
            if idade > 0:
                return idade
            else:
                print('idade invalida')
        except ValueError :
            print('cadastre apenas idades positivas com numeros inteiros exemplo 1,2,3,4,5')
        
def continuar():
    while True:
        opc = input('deseja continuar (s/n):')
        if opc == 'n':
            return True
        elif opc == 's':
            return False
        else:
            print('opção invalida')


registro_pessoas = []
soma = 0 
while True:
    nome_usuario = registrar_nome()
    sexo_usuario = registrar_sexo()
    idade_usuario = registrar_idade()
    registrar_pessoa = {
        'nome':nome_usuario,
        'sexo':sexo_usuario,
        'idade':idade_usuario
    } 
    registro_pessoas.append(registrar_pessoa)
    if continuar():
        break
print(f'total de usuarios cadastrados: {len(registro_pessoas)}')
soma = 0
for i in registro_pessoas:
    for x in i.values():
        if isinstance(x,int):
           soma += x

media = soma / len(registro_pessoas)

print(f'media das idades: {media}')


for i in registro_pessoas:
    if i['sexo'] == 'f':
        print(f'mulheres do grupo\n{i}')
    
for i in registro_pessoas:
    if i['idade'] > media:
        print(f'usuarios que tem idade acima da media\n{i}')
    
