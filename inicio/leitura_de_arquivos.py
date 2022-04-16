"""
Leitura de Arquivos

para o conteudo de um arquivo em Python utilizamos a função integrada open(),
que literalmente significa 'abrir'.

open() -> Na forma mais simples de utilização nós passamos apenas um parametro
de entrada, que neste caso é o caminho para o arquivo a ser lido. essa função retorna
um _oi.TextIOWrapper e é com ele que trabalhamos então.

https://docs.python.org/3/library/functions.html#open

#OBS: esse arquivo deve existir



"""

# exemplo

arquivo = open('texto.txt')

print(arquivo)

arquivo.close()

"""
with open(texto.txt) 
ira escrever dentro do txt


"""
with open('texto1.txt', 'w') as arquivo:
    arquivo.write('iouasd\n')
    arquivo.write('asndfkjsanvsgnsdmndksfvbkdjsfvbdvbmnknnjngvbknvn\n')
    arquivo.white('oi')
