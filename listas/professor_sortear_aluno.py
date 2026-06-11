'''Um professor quer sortear um aluno para responder uma questão:
alunos = ["Ana", "Bruno", "Carlos", "Daniela"]
• Misture a ordem dos alunos
• Escolha um aluno aleatoriamente'''
import random
alunos = ["Ana", "Bruno", "Carlos", "Daniela"] 
escolhido = random.choice(alunos)
print(f'o escolhido foi {escolhido}')
