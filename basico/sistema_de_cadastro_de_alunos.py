'''Sistema de cadastro de alunos
Funções obrigatórias:
• Cadastrar nome do aluno
• Permitir cadastrar vários alunos (repetição)
• Mostrar lista de alunos cadastrados'''
while True :
    print('digite x para finalizar')
    alunos = input('digite seu nome ')
    if alunos == 'x' :
        break
    for i in range(1) :
        print(f'aluno cadastrado: {alunos}')
