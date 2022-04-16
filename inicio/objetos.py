"""
Poo

Objetos sao instancias da classe. Ou sea, apos o mapeamento do objeto do mundo real para sua represntacao computacional devemos poder criar uantos objetos forem
necessarios. Podemos pensar nos objetos/instancias de uma  classe como variaveis do tipo definido na classe.
"""


class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampada(self):
        return self.ligada

    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True


class ContaCorrente:
    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha

nome = 'arthur'
sobrenome = 'henrique'
email = 'arthur.henrique.elias@gail.com'
senha = 'arthur9826'

user = Usuario(nome, sobrenome, email, senha)
print(f' eu sou {nome}')

