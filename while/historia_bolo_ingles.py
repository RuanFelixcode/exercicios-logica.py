'''Escreva um algoritmo para perguntar ao usuário se ele “Gostaria de Ler uma História? 1.Sim
2.Não”. Se ele responder “1”, o algoritmo deve escrever na tela “Era uma vez um bolo inglês, quer
que eu conte outra vez?”. E ler a resposta novamente. Enquanto o usuário responder “1.Sim” para a
pergunta, o algoritmo deve escrever a história, quando o usuário responder “2.Não”, o algoritmo deve
ser encerrado escrevendo “Fim” na tela'''
while True:
    pergunta = int(input('''Gostaria de Ler uma História? 1.Sim
2.Não”.'''))
    if pergunta == 1:
        print('''Era uma vez um bolo inglês, quer
que eu conte outra vez?''')
        continue
    elif pergunta == 2:
        print('fim')
        break
    else:
        print('selecione uma opçao valida')
