'''Questão 8 – Idade, Altura e Peso de 10
Pessoas
O algoritmo deve:
• Ler idade, altura e peso de 10 pessoas
• Calcular:
o Quantidade de pessoas com idade superior a 50 anos
o Média das alturas das pessoas entre 10 e 20 anos
o Porcentagem de pessoas com peso menor que 40 kg'''
maior_50 = 0
soma = 0
divisor = 0
total = 0
total2 = 0
for i in range(10):
    idade = int(input('digite sua idade:'))
    peso = float(input('digite seu peso:'))
    altura = float(input('digite sua altura:'))
    total += 1
    if idade > 50:
        maior_50 += 1
    if idade >= 10 and idade <= 20:
        divisor += 1
        soma = altura + soma
    if peso < 40 :
        total2 += 1
if divisor > 0 :
    print(f'media das pessoas entre 10 a 20 anos {soma/divisor}')
else:
    print('nenhuma pessoa com idade entre 10 e 20 ')
print(f'o Porcentagem de pessoas com peso menor que 40 kg {(total2/total)*100}')
