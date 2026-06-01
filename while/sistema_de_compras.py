'''1. Sistema de compras
Em um mercado, o caixa registra os valores dos produtos comprados. O sistema deve:
• Solicitar o valor de vários produtos
• Quando o usuário digitar 0, a compra é encerrada
• Mostrar o valor total da compra
Regra: valores negativos devem ser ignorados'''
prt = float(input('digite o valor do produto '))
soma = 0
while prt != 0 :
    if prt < 0 :
        print('saldo insuficiente')
    else:
        soma = soma + prt 
    print('digite 0 para parar')
    prt = float(input('digite o valor do produto '))
print(f'valor total {soma:.2f} ')
