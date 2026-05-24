'''Crie uma classe chamada Produto. Essa classe deve representar um produto e deve
armazenar as seguintes informações: nome, preço e quantidade em estoque.
Além disso, crie um método chamado mostrar_produto() que exiba todas as
informações do produto de forma organizada na tela.
Após criar a classe, instancie um objeto informando os dados do produto. Em seguida,
execute o método para exibir as informações.

A saída do programa deve seguir um formato semelhante a este:
Produto: Caderno
Preço: 10.0
Quantidade: 5'''

class Produto :
    def __init__ (self,nome,preco,quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        
    def exibir(self):
        print(self.nome,self.preco,self.quantidade)
    
    def verificar(self):
        if self.quantidade > 0:
            print('produto disponivel')
        else:
            print('produto nao disponivel')
            
produto1 = Produto('caderno',10.0,5)
produto1.exibir()
produto1.verificar()
