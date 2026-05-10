class Livro:
    def __init__(self,titulo,autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel =  True
    def mostrar_info(self):
        if self.disponivel:
            print(f'itens disponiveis titulo:{self.titulo}\nautor:{self.autor}')
        else:
            print('n esta disponivel')
    
    def emprestar(self):
        self.disponivel = False
        
    def devolver(self):
        self.disponivel = True
         
        
livro1 = Livro('livro generico','autor generico')
livro1.mostrar_info()
livro1.emprestar()
livro1.mostrar_info()
print('=-'*30)
livro1.devolver()
livro1.mostrar_info()
