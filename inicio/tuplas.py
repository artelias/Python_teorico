"""
Tuplas (tuple)

Tuplas são bastantes parecidas com listas.

Existem basicamente duas diferenças básicas:

1 - As tuplas são representadas por parênteses ()

2 - As tuplas são imutáveis: Isso significa que ao se criar uma tupla ela não muda. Toda operação com uma tupla
gera uma nova tupla.

# CUIDADO 1: As tuplas são representadas por (), mas veja:
tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)

print(type(tupla2))

#CUIDADO 2: Tuplas com 1 elemento

tupla3 = (4)

print(tupla3)# não é uma tupla
print(type(tupla3))
tupla4 = (4, )# é uma tupla
print(type(tupla4))

#conclusão podemos concluir que tplas são definidadas por virgulas e não por parêntese

#tupla támbem funciona com range

tupla = tuple(range(11))
print(tupla)

#MAXIMO, MINIMO SOMA E TAMANHO SÓ FUNCIONAM EM REAIS OU INTEIROS

tupla=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

#podemos sobrepor e soma as tuplas mas n auteramos o conteudo em sí
tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tupla2 = (11, 12)
print(tupla + tupla2)

#verificando se determinado elemento está contido na tupla

tupla = (1 ,2, 3)

for n in tupla:
    print(n)

    for indice, valor in enumerate(tupla):
        print(indice, valor)

#contando elementos dentro de uma tupla

tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')
print(tupla.count('c')) #QUANTOS TEM DE 'C'

# Dica na utilização de tuplas

# Devemos utulizar tuplas SEMPRE que não precisamos modificar os dados contiidos em uma coleção

# Exemplo 1

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

print(meses)

#acesso aos elementos da tupla é iguala da lista.

#iteração com while
i = 0

while i < len(meses):
    print(meses[i])
    i = i + 1
"""

#Por quê utilizar tuplas?

# - Tuplas são mais rápidas do que listas.

# - Tuplas deixam seu codigo mais seguro*.
#* trabalha com elementos imutaveis traz segurança para seu código.