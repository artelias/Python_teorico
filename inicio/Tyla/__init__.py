from csv import reader

with open("bre.csv") as arquivo:
    dados = arquivo.read()
    dados = dados.split(',')[2:]
    print(dados)
