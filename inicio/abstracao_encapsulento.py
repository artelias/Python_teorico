"""
POO - Abtracao e encapsulamento

O grande objetivo da POO e encapsular nosso codigo dentro de um grupo logico e hierarquico utilizando classes.
sss
Abstracao , em POO, e o ato de expor apenas dados relevantes de uma classe, escondendo atributos e metodos
privados de usuario






"""

class Conta:
    contador = 400
    def __init__(self,titular, saldo, limite):
        self.numero = Conta.contador
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.saldo} do titular {self.titular} com limite de {self.limite}')

    def depositar(self,valor):
        if valor > 0:
            self.saldo += valor
        else:
            print('o valor precisa ser positivo')

    def sacar(self,valor):
        if valor > 0:
           if self.saldo >= valor:
               self.saldo -= valor
           else:
               print('saldo insuficiente')
        else:
            print("o valor deve ser positivo")
    def transferir(self,valor, conta_destino):
        self.saldo -= valor
        self.saldo -= 10
        
        conta_destino.saldo += valor

conta1 = Conta('arthur',150.00, 1500)
print(conta1.__dict__)

conta1.extrato()

conta2 = Conta('felipe',200.00,1000)

print(conta2.__dict__)
conta2.extrato()

conta2.transferir(100,conta1)
print(conta1.__dict__)
print(conta2.__dict__)