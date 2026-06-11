idade = int(input('digite sua idade:'))
while True:
    permiçao_medica = input('voce tem permiçao medica (s pra sim n pra nao)')
    if permiçao_medica == 's' or permiçao_medica == 'n':
        break 
    print('digite uma opçao valida')
if idade >=18 and idade <= 35 and permiçao_medica == 's':
    print('voce tem permiçao pra competir')
else:
    print('voce nao pode competir')
