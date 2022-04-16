"""
Funções de maior grandeza

Oque isso significa?

- Quando uma linguagem de programação suporte HOF, indica que podemos ter funções
que retornam outras funções, e atémesmo criar variáveis do tipo de funções
nos nossos programas.

OBS: Na seção de funções, nós utilizamos isso.

# Exemplo - Definindo as funções

def somar(a,b):
    return a + b

def subtrair(a,b):
    return a - b
def multiplicar(a,b):
    return a * b
def dividir(a,b):
    return a / b
def calcular(num1,num2,funcao):
    return funcao(num1,num2)

#em python podemos ter funções dentro de funções
"""

# Exemplo
from  random import choice
def cumprimeneto(pessoa):
    def humor():
        return choice(('e ai ', 'suma daqui ', 'sucumba '))
    return humor() + pessoa

print(cumprimeneto('angela'))

def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar

@gritar
def saudacao(nome):
    return f'Olá, eu sou 0/a {nome}'

@gritar
def ordenar(principal, acompanhamento):
    return f'olá, eu gostaria de {principal} acompanhado de {acompanhamento}, por favor.'

print(saudacao('Felicity'))