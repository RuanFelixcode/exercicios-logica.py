class Gafonhoto:
    def __init__(self):
        self.nome = ''
        self.idade = 0
    def aniversario(self):
        return f'aniversaro de {self.nome} completa hoje {self.idade}'
        
g1 = Gafonhoto()
print(g1.aniversario())
g1.nome = 'ruan'
g1.idade = 18
print(g1.aniversario())

        
