class Carro:
    def __init__ (self,nome,cor,velocidade,tamanho,peso):
        self.nome = nome
        self.cor = cor
        self.velocidade = velocidade
        self.tamanho = tamanho
        self.peso = peso
    def mostrar_carro(self):
        print(f'''nome:{self.nome}\ncor:{self.cor}\nvelocidade atual:{self.velocidade}\ntamanho:{self.tamanho}\npeso:{self.peso}''')
    def alterar_velocidade(self):
        self.velocidade = botao = float(input('altere a velocidade:'))
ferrari =  Carro('carro bonito','azul',10.0,4.20,900)
ferrari.mostrar_carro()
ferrari.alterar_velocidade()
ferrari.mostrar_carro()
