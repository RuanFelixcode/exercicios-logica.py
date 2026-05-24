class Conta:
    def __init__(self,saldo = 0,titular = ''):
        self.__saldo = saldo # nao mexer aqui
        self.__titular = titular
    def depositar(self):
        valor_positivo = float(input('digite o valor do deposito:'))
        if valor_positivo > 0:
            self.__saldo += valor_positivo
        else:
            print('nao aceitamos valores negativos')
    
    def sacar(self):
        saque = float(input('digite o quanto deseja sacar:'))
        if saque <= self.__saldo:
            self.__saldo -= saque
        else:
            print('saque exede limite da conta')
            
    
    def mostrar_saldo(self):
        print(f'saldo atual:{self.__saldo}')
        
conta1 = Conta(50,'lucas')
conta1.mostrar_saldo()
conta1.depositar()
conta1.mostrar_saldo()
conta1.sacar()
conta1.mostrar_saldo()
conta1 = Conta(50, 'lucas')
# Tentando acessar diretamente o saldo
# print(conta1.__saldo)   # Isso vai dar erro: AttributeError


              
    
    
