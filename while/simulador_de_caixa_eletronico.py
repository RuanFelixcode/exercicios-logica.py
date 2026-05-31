'''Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''



total_1 = 0
total_2 = 0
total_3 = 0
total_4 = 0

valor_saque = int(input('digite o valor do saque:').strip())

while valor_saque >= 50:
    valor_saque -= 50
    total_1 += 1

while valor_saque >= 20:
    valor_saque -= 20
    total_2 += 1
    
while valor_saque >= 10:
    valor_saque -= 10
    total_3 += 1
    
while valor_saque >= 1:
    valor_saque -= 1
    total_4 += 1
    
print(f'''total notas de 50$ {total_1}\ntotal notas de 20$ {total_2}\ntotal notas de 10$ {total_3}\ntotal notas de $1 {total_4}''')
    
    

