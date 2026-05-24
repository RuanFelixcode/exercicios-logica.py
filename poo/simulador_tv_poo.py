class Tv:
    def __init__(self):
        self.canais = ['Globo', 'Record']
        self.volume = 0
        self.ligado = True
        self.canal_atual = "tela preta"
    def exibir(self):
        if self.ligado:
            print(f"Canais: {self.canais}\nCanal: {self.canal_atual}\nVolume: {self.volume}\nEstado: TV Ligada")
        else:
            print("TV desligada")
    def alterar_volume(self):
        if self.ligado:
            try:
                volume = int(input("digite o novo volume:"))
                if volume < 0 :
                    print("não é permitido volume negativo")
                elif volume > 100:
                    print('nao e permitido volume maior que 100')
                else:
                    self.volume = volume
            except ValueError:
                print("erro")
        else:
            print("TV desligada")
    def mudar_canal(self):
        if self.ligado:
            alterar = input("escolha o canal:")
            if alterar in self.canais:
                self.canal_atual = alterar
            else:
                print("canal não esta na lista")
           
    def ligar_tv(self):
        if self.ligado:
            print("tv ja esta ligada")
        else:
            print('ligando tv')
            self.ligado = True
    def desligar(self):
        if self.ligado:
            self.ligado = False
        else:
            print("TV ja esta desligada")
    def adicionar_canal(self):
        novo_canal = input('digite o nome do novo canal:')
        if novo_canal in self.canais:
            print('canal ja existe')
        else:
            self.canais.append(novo_canal)
            
positivo = Tv()
positivo.desligar()
print('='*40)
positivo.exibir()
print('='*40)
positivo.desligar()
print('='*40)
positivo.ligar_tv()
print('='*40)
positivo.exibir()
print('='*40)
positivo.mudar_canal()
print('='*40)
positivo.exibir()
print('='*40)
positivo.alterar_volume()
print('='*40)
positivo.exibir()
print('='*40)
positivo.adicionar_canal()
print('='*40)
positivo.exibir()

