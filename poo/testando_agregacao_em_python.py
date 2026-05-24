class Motor:
    def __init__(self,peso,tamanho):
        self.peso = peso
        self.tamanho = tamanho
class Rodas:
    def __init__(self,qtd):
        self.qtd = qtd
motor_do_carro = Motor(10,20)
rodas_do_carro = Rodas(4)

class Carro:
    def __init__(self,modelo,marca):
        self.modelo = modelo
        self.marca = marca 
        self.motor_de_todos_os_carros = motor_do_carro
        self.quantidade_de_rodas = rodas_do_carro
carro1 =  Carro('fusca','Volkswagen.') 

print(carro1.quantidade_de_rodas.qtd)

        
