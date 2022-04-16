"""
POO - Polimorfismo

Poli -> Muitas
Morfis -> Formas


"""


class Animal(object):

    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError('A classe filha precisa implemenar este metodo')

    def comer(self):
        print(f'{self.__nome} esta comendo...')


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala au au')


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala miau miau')


class Rato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f"{self._Animal__nome} fala n sei")


felix = Gato('Felix')
felix.comer()
felix.falar()

pluto = Cachorro('pluto')
pluto.comer()
pluto.falar()

michael = Rato('michael')
michael.falar()
michael.comer()
