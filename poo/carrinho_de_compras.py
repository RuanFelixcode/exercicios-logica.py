class Carrinho_de_compras:
    def __init__(self):
      self.nome = ''
      self.preco = 00.00
      self.quantidade = 0
      self.carrinho = {} 
    def produtos_add_ao_carrinho(self):
       self.nome  = nome = input('digite o nome do produto:')
       self.preco = preco = float(input('digite o preço do produto:'))
       self.quantidade = quantidade  =  int(input('digite a quantidade:'))
       self.carrinho.update({self.nome:self.quantidade})

   
    def remover_produtos_do_carrinho(self):
       nome_produto = input('digite o produto que quer remover:')
       self.carrinho.pop(nome_produto)
       
    def total(self):
       print(f'exibindo produto carrinho:{self.carrinho}')
       print(f'calculando...\n preço x quantidade\nresultado = {self.preco*self.quantidade}')
       
       

carinho1 = Carrinho_de_compras()
carinho1.produtos_add_ao_carrinho()
carinho1.total()
carinho1.remover_produtos_do_carrinho()
carinho1.total()
