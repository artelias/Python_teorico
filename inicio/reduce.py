"""
Reduce

Boa opção quando n quiser usar loop for

para entender o reduce()

# Imagina que você tem uma coleção de dados:
dados = [a1, a2 , a3, ..., an]
# e você tem uma função que recebe dois parâmetros

def funcao(x, y):
    return x * y

    assim como map() e filter(), função reduce() recebe dois parametro: a função e o iteravel

reduce(funcao, dados)

A função reduce (), funciona da seguinte forma:
   passo 1: res1 = f(a1, a2) # aplica a função nos dois primeiros elementos da coleção e guarda o resultado.
   passo 2: res2 = f(res1, a3) # aplica a função passando o resultado do passo1 mais o terceiro elemento e guarda o resto

   Isso é reétido até o final.
   passo 3: res3 = (s2, a4)
   .
   .
   .

    ou sejam em cada passo ela aplica a funçao passando como primeiro argumento p resiçtadp da aplicaçap anterior. no final, reduce() irá reornar o resultado final.

alternativamente, poderiamos ver a função reduce() como:

funcao(funcao(a1, a2), a3),a4), ...), an)
"""

# como funciona na pratica?

#vamos utilizar a função reduce() para multiplicar todos ps numeros de uma lista

from functools import reduce

dados = [2, 3, 4, 5, 6, 7, 8, 9, 10]

#para utilizar o reduce() nós precisamos de uma função que receba dois parâmetros
multi = lambda x, y: x * y

res = reduce(multi, dados)
print(res)
# ocorreu a multiplicação de todos os membros
