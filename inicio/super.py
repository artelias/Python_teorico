"""
POOO - O metodo super()

o metodo super () se refere  super classe.


"""

class Animal:
    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def faz_som(self, som):
        print(f'O {self.__nome} fala {som}')

class Gato(Animal):
    def __init__(self, nome, especie, raca):
        super().__init__(nome,especie)
        self.__raca = raca


felix = Gato('Felix','Felino', 'Angara')
felix.faz_som('miau')