class Aluno :
    def __init__ (self,nome,idade,nota):
        self.nome = nome
        self.idade = idade
        self.nota = nota
        
    def mostrar_aluno(self):
        print(f'{self.nome}\nidade:{self.idade}\nnota:{self.nota}')
        
    def verificar_aprovacao(self):
        if self.nota >= 7:
            print('aprovado')
        else:
            print('reprovado')
ruan = Aluno('ruan',18,10)
marcos = Aluno('marcos',19,5)
ruan.mostrar_aluno()
ruan.verificar_aprovacao()
print('-='*30)
marcos.mostrar_aluno()
marcos.verificar_aprovacao()

        
