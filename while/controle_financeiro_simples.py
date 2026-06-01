'''5. Controle financeiro simples
Um usuário registra suas movimentações:
• Valores positivos = entrada de dinheiro
• Valores negativos = saída
• O programa para quando digitar 0
Mostrar:
• Total de entradas
• Total de saídas
• Saldo final'''
Totalp = 0
totaln = 0
while True :
    saldo = float(input('digite valores ')) 
    if saldo == 0 :
        break
    elif saldo > 0:
        Totalp = saldo + Totalp
    elif saldo < 0 :
        totaln = saldo - totaln
saldo_at = totaln + Totalp
print(f'Total de entradas {Totalp:.2f}')
print(f'Total de saídas {totaln:.2f}')
print(f'total {saldo_at} ')
