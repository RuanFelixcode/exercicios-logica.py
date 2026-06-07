def continuar():
    while True:
        opc = input('deseja continuar (s/n):')
        if opc in ('n','não','nao'):
            return True
        elif opc in ('s','sim'):
            return False
        else:
            print('opção invalida')

class Livro:
    def __init__(self):
        self.titulo = ''
        self.autor = ''
    
    def criar_livro(self):
        self.titulo = input('digite o titulo do livro:')
        self.autor = input('digite o autor do livro:')
        
    
class Bliblioteca:
    def __init__(self):
        self.estante = []

    def listar_livros(self):
        ids = 0
        for i in self.estante:
            print(f'titulo:{i.titulo}\nautor:{i.autor}\nid {ids}')
            ids += 1
        
    def adicionar_livros(self):
        while True:
            novo_livro = Livro()
            novo_livro.criar_livro()
            ja_existe = False
            for livro_salvo in self.estante:
                if livro_salvo.titulo == novo_livro.titulo:
                    ja_existe = True
                    break
            if ja_existe:
                print('livro ja existe')
                continue
            else:
                self.estante.append(novo_livro)
            print('novo livro?')
            if continuar():
                break
    def remover_livro(self):
        while True:
            self.listar_livros()
            try:
                remover = int(input('digite o id do item que deseja remover:'))
                self.estante.pop(remover)
                print('remover outro livro?')
                if continuar():
                    break
            except ValueError:
                print('digite somente numeros inteiros\nexemplos\n1,2,3,4,5')
            
            except IndexError:
                print('id não existe por favor digite um id valido')
Blibliotecario = Bliblioteca()
while True:
    while True:
        print('menu do blibliotecario\nopções\n1 - listar livros\n2 - adicionar_livros\n3 - remover_livro')
        try:
            opc = int(input('selecione a opção:'))
            if opc == 1:
                Blibliotecario.listar_livros()
            elif opc == 2:
                Blibliotecario.adicionar_livros()
            elif opc == 3:
                Blibliotecario.remover_livro()
            else:
                print('opção invalida')
            print('menu novamente?')
            if continuar():
                print('sistema encerado')
                break
        except ValueError:
            print('digite somente caracteres de numeros inteiros')

