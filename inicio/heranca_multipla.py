"""
POO - Heranca multipla

Heranca multipla nada mais eh do que a posibilidade de uma classe herdar de multiplas classes, fazendo com que a classe filha herde todos os atributos e metodos de todas as classes herdadas.

#OBS: A heranca multipla pode ser feita de duas maneiras:
    - Por Multiderivacao Direta
    - Por Multiderivacao Indireta
    # exemplo 1 - Multriderivacao direta
class Base1:
    pass
class Base2:
    pass
class Base3:
    pass
class MultiDerivada(Base1,Base2,Base3):
    pass

# exemplo 2 Multiderivacao Indireta

class Base1:
    pass
class Base2(Base1):
    pass
class Base3(Base2):
    pass
class MultiDerivada(Base1,Base2,Base3):
    pass
"""
