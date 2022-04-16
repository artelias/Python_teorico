"""
Lendo arquivos CSV

CSV - Comma Separeted Values - Valores Separados por Virgula

1,2,3,4,5,6,7,8,9

1;2;3;4;5;6;7;8;9

 1 2 3 4 5 6 7 8 9

file = open(filename, encoding="utf8") pra abrir um arquivo

"""
from csv import reader

with open('lutadores.csv', encoding="utf8") as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv)
    for linha in leitor_csv:
        print(f'{linha[0]} nasceu no {linha[1]} e mede {linha[2]} centimetros')
