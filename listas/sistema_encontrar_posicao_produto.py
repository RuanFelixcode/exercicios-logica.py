'''Um sistema precisa encontrar a posição de um produto:
produtos = ["TV", "Celular", "Notebook"]
Verifique se "Celular" está na lista e, se estiver, mostre sua
posição.'''
produtos = ["TV", "Celular", "Notebook"]
guarda = str
for i in produtos:
    if i == "Celular":
        guarda = produtos.index("Celular")
print(f'esta na posiçao {guarda}')
