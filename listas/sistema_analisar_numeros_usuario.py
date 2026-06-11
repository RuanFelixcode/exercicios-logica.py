'''8.
Um sistema precisa analisar números digitados pelo usuário.
Crie um programa que:
• Leia números até o usuário digitar 0
• Armazene na lista
• Depois percorra a lista e:
o Conte quantos são positivos
o Conte quantos são negativos'''
lista = []
while True:
    n = int(input('digite um numero:'))
    if n == 0 :
        break
    lista.append(n)
cont = 0 
contn = 0 
for i in lista:
    if i > 0 :
        cont += 1 
    elif i < 0 :
        contn += 1
print(f'total de numeros positivos {cont}')
print(f'total de numeros negativos {contn}')

