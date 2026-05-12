class Funcionario:
   def __init__(self,nome,salario):
        self.nome = nome
        self.salario = salario
      
   def mostrar_dados(self):
    print(f'nome {self.nome} saldo: {self.salario}')
   
class Gerente(Funcionario):
   def aprovar_ferias(self,junior):
      print(f'suas ferias foram aprovadas {junior.nome}')

class Dev (Funcionario):
   def programar(self):
      print(f'{self.nome} esta programando')
      
programador1 = Dev('ruan',10000)
gerente1 = Gerente('carlos',1000000000000000)
programador1.mostrar_dados()
gerente1.mostrar_dados()
print('-='*30)
programador1.programar()
print('-='*30)
gerente1.aprovar_ferias(programador1)
