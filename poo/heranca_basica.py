class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    def apresentar(self):
        print(f'ola meu nome e {self.nome} e minha idade e {self.idade}')
        
        
pessoa1 = Pessoa('generico',0)
pessoa1.apresentar()

class Aluno (Pessoa):
    def __init__(self,nome,idade,estudar): 
        super().__init__(nome,idade) 
        self.estudar = estudar
    def curso(self):
        print(f'aluno {self.nome} esta estudando {self.estudar}')
        
        
aluno1 = Aluno('ruan',18,'programaçao')
aluno1.curso()
aluno1.apresentar()
