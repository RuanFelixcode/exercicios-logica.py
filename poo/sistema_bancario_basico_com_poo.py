class Banco:
    def __init__(self):
        self.titular = ''
        self.saldo = 0.00                                          
    def registrar_nome(self):
        while True:
            nome = input('digite seu nome:')
            if not nome.replace(' ','').isalpha():
                print('nao aceitamos nomes com numeros digite apenas nomes simples ou compostos')
                continue
            else:
                self.titular = nome
                break
    def depositar(self):
        while True:
            try:
                valor = float(input('digite o valor do deposito:'))
                if valor < 0:
                    print('por favor digite apenas saldo positivo')
                else:
                    self.saldo +=  valor
                    break
                    
            except ValueError:
                print('deposite o saldo apenas com valores numericos')
    def saque (self):
        while True:
            try:
                saque = float(input('digite o valor do saque:'))
                if saque <= self.saldo:
                    self.saldo -= saque
                    break
                else:
                    print('valor do saque excede o valor do saldo')
                    continue
            except ValueError:
                print('digite o valor do saque digitando numeros')
    def exibir_conta(self):
        print(f'nome do usuario:{self.titular}\nsaldo atual:{self.saldo}')
usuario1 = Banco()
usuario1.registrar_nome() 
usuario1.depositar()
usuario1.saque()
usuario1.exibir_conta()
usuario2 = Banco()
usuario2.registrar_nome() 
usuario2.depositar()
usuario2.saque()
usuario2.exibir_conta()
