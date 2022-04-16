"""
Conjuntos

- Conjuntos em qualquer linguagem de programação, estamos fazendo referencia a teoria dos conjuntos da matematica.

- Aqui no pythonm os conjuntos são chamados de Sets.

Dito isto, da mesma forma que na matemática:

- Sets (conjuntos) não possuem valores duplicados;
- Sets (conjuntos) não possuem valores ordenados;
- Elementos não são acessados via índice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos
mas não nos importamos com a ordenação deles. Quando não precisamos se preocupar com chaves, valores e itens duplicados.

OS conjuntos (sets) são referenciados em python com chaves{}

Diferença entre conjuntos (set) e mapas (dicionários) em Python:
    -Um dicionário tem chave/valor;
    -Um conjunto tem apenas valor;


# Definindo um conjunto:

# Forma 1

s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})# temos valores repetidos.

print(s)

#conjuntos ignoram valores repetidos

# Forma 2

s = {1, 2, 3, 4, 5 ,5 ,5, 5}
print(s)

#repitições são ignoradas

if 3 in s:
    print('tem o 3')
else:
    print('não tem o 3')
"""

f = {1, 3, 5, 6, 4, 3}
print(f)
print(type(f))