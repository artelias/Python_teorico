"""
Modulo radom e o que são módulos

- Em python, mnodulos nada mais são do que arquivos python.

modulo radom -> Possui vários funções para geração de números pseudo-aleatorios

#OBS: Existem duas formas de se utilizar um modulo ou função deste

# forma 1- importando todo o modulo.

import random

# Ao realizar o import ede todo modulo, todas as funções, atobitos, classes e propriedades que estiverem
# dentro do módulo ficarão disponiveis(ficaram na memoria).

print(random.random()) #gera numeros entre (0,1)
************************************************************************************************************************
#forma 2- importando função especifica do modulo

from random import random

for i in range(10):
    print(random())
************************************************************************************************************************
from random import uniform

for i in range(10):
    print(uniform(3,7))# uniforme e um random com valor definido pelo programador

# randint() -> Gera valores pseudo-aleatorios entre os valores estabelecidos.
from random import randint

# gerador de apostas para mega-sena
for i in range(6):
    print(randint(1, 61), end=',')  # de 1 a 60

#choice() -> Mostra um valor aleatorio entre iteravel
from random import choice
jogadas = ['pedra', 'papel', 'tesoura']

print(choice(jogadas))

from random import shuffle

#shuffle() -> tem a função de embaralhar dados

cartas = ['K','Q','J','A','2','3','4','5','6','7','8','9']

print(cartas)

shuffle(cartas)

print(cartas[0]) 
"""

