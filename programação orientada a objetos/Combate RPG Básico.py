class Personagem:
    def __init__(self,nome):
        self.nome = nome
        self.vida = 100
        self.ataque = 20
    def status (self):
        print('=-'*30)
        print(f'nome do jogador:{self.nome}\npontos de vida:{self.vida}\natributos de ataque:{self.ataque}')
        print('=-'*30)
    def atacar(self):
        print(f'{self.nome} fez um ataque de {self.ataque} de dano') 
        
    def levar_dano(self):
        self.vida -= self.ataque
        
jogador1 = Personagem('ruan')
jogador2 = Personagem('rafael')
jogador1.status()
jogador2.status()
jogador1.atacar()
jogador2.levar_dano()
jogador2.status()
