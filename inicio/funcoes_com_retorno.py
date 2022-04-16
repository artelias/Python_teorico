"""
Funções com retorno

OBS: se não retorna ela é do tipo None

OBS: funções em Python que retornam valores devem usar a palavra return


"""

# Exemplo função
def quadrado_de_7():
    return 7*7

quadrado_de_7()
print(quadrado_de_7())

from random import random
def jogar_a_moeda():
    valor = random()
    if valor > 0.5:
        return 'cara'
    else:
        return 'coroa'

print(jogar_a_moeda())