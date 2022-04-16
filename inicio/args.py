"""
*arg é qualquer argumento em uma função, entrados com uma tupla

#exemplo 1
def soma_todos_numeros(num1, num2, num3):
    return num1 + num2 + num3
print(soma_todos_numeros(4, 6, 9))

"""


# exemplo 2
def soma_todos_numeros(*args):
    total = 0
    for numero in args:
        total = total + numero
    return total


print(soma_todos_numeros(3, 4, 5, 5))


# ou
def soma(*args):
   return sum(args)


print(soma(5, 3))
