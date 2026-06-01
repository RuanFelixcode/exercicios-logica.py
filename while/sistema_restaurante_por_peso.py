'''Restaurante por peso
Um restaurante cobra por quilo. O sistema deve:
• Ler o peso do prato de vários clientes
• Encerrar quando o peso for 0
• Ignorar pesos negativos
• Calcular o peso total servido no dia'''
cont = 0
peso = float(input('digite o peso do prato '))
while peso != 0 :
    
    if peso < 0 :
        print ('peso invalido')
    else:
        cont = cont + peso
    peso = float(input('digite o peso do prato '))
    
    
       
    
print(f'total {cont:.2f}')
