class Personagem:
    def __init__(self,nome,vida):
        self.nome = nome
        self.vida = vida
        
    def status(self):
        print(f'nome do Personagem: {self.nome }\natributos de vida: {self.vida}')
npc = Personagem('sem nome',20)
npc.status()
class Mago(Personagem):
    def __init__(self,nome,vida,mana):
        super(). __init__(nome,vida)
        self.mana = mana
    def soltar_magia(self):
        print(f'preparando magia... total de mp:{self.mana}')
        self.mana -= 5
        print(f'Personagem:{self.nome} soltou uma bola de fogo -5 mp:{self.mana}')
        
jogador1 = Mago('lucas',10,50)
jogador1.status()
jogador1.soltar_magia()

class Guerreiro(Personagem):
    def __init__(self,nome,vida,forca):
        super(). __init__ (nome,vida)
        self.forca = forca
    def golpe(self):
        print(f'preparando golpe de espada... força total sem armas {self.forca}')
        print(f'Personagem:{self.nome} deu um golpe de espada +{self.forca+10} de dano')
        
jogador2 = Guerreiro('italo',50,100)
jogador2.status()
jogador2.golpe()





        
