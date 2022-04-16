"""
PEP8 - Python Enhancement Proposal

são prospostas de melhorias para a linguagem python

zem of python

import this

A ideia da pep8 é que possamos escrever codigo Python de forma Pythônica.

{1} - utilize Camel Case para nome de classes

class Calculadora:
    pass


class Calculadoracientifica:
    pass

{2} - Utilize nomes em minúsculo, separados por underline para funções ou variáveis:

def soma():
    pass


def soma_dois():
    pass


numero = 4
numero_impar = 5
{3} - Utilize 4 espaços para identação!

if 'a' in 'banana':
    print('tem')

{4} - Linhas em branco
-separa funçoes e definições de classes com duas linhas em branco:
-Metodos dentro de uma classe devem ser separados com uma única linha em branco;
class Classe:
    pass

class Outra:
    pass
{5} - Imports
- Imports devem ser sempre feitos em linhas separadas;
# Import certo
import sys
import os

#não a problemas em utilizar:
from types import StringTypel, ListType
#Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:

from types import(
    StringType,
    ListType,
    SetType,
    OutroType
)
#Imports devem ser colocados no topo do arquivo, logo depois de quaisquer cometários ou docstrings e
#antes de constantes ou variáveis globais
{6} - Espaços em empressões e instruções
#não faça:
função( algo[ 1 ], { outro: 2 } )
#faça:
funcao(algo[1], {algo:2})

#não faça:
algo (1)
#faça:
algo(1)
#não faça:
x         =3
y         =5
variavel l=23
#faça:
x=1
t=3
{7} - termine funções e coloque uma linha
"""







