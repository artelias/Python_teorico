"""
lambdas são funcoes anonimas, ou seja sem nome

# Função em Python
def soma (a, b):
    return a + b

#expressão lambda
lambda x: 3 * + 1

#como utlizar a expressão lambda?
calc = lambda x: 3 * x + 1

print(calc(4))


"""

#f(x) =  a * x ** 2 + b * x + c

def geradora_de_funcao_quadratica(a, b, c):
    return lambda x: a * x ** 2 + b * x + c

teste = geradora_de_funcao_quadratica(1, 4, 5)
print(teste(2))

