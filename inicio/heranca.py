"""
POOO - Heranca

A ideia de heranca eh a ideia de reaproveitar codigo . tambem de extender nossas classes.

OBS: Com a heranca, a partir de uma classe existente, nos extendemos outra classe
que passa a herdar atributos emetodos da classe herdada

Cliente
    -nome
    -sobrenome
    -cpf
    -renda

Funcionatio
    -nome
    -sobrenome
    -cpf
    -matricula

class Cliente():

    def __init__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Funcionario():

    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


cliente1 = Cliente('Arthur', 'Henrique', '107.014.444-44', 2000)
funcionario1 = Funcionario('Felipe', 'Gabriel', '123.234.345-45', 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())

Obs: Quando uma clase herdade outra classe ela gerda todos os atributos e metodos da classe gerdada

quando uma classe herda de oputra classe, a classe herdada e conhecida por:
    [Pessoa]
    -Super classe
    -Classe mae
    -classe pai
    classe generica

Quando uma classse herda outra classe
    -sub classe
    -classe filha
    -classe especifica
"""
class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

class Cliente(Pessoa):

    def __init__(self,nome,sobrenome,cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda

class Funcionario(Pessoa):

    def __init__(self,nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula


class pinguim:
    def ___init__(self,nome,sobrenome):
        self.__nome = nome
        self.__sobrenome = sobrenome
cliente1 = Cliente('Arthur', 'Henrique', '107.014.444-44', 2000)
funcionario1 = Funcionario('Felipe', 'Gabriel', '123.234.345-45', 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())
