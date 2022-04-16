"""
Map

import math


def area(r):
    #area de um circulo
    return math.pi * (r ** 2)


print(area(2))

raios = [2, 5, 7.1, 0.3, 10, 44]

# Forma comum
areas = []
for r in raios:
    areas.append((area(r)))

print(areas)

# Forma 2 - map

# Map é uma função que recebe dois parametros: o primeiro a função, o segundo iteravel. retorna um map objeto

areas = map(area, raios)

print(areas)
print(type(areas))
print(list(areas))

# Forma 3 - Map com Lambda
print(list(map(lambda r: math.pi * (r ** 2), raios)))

#zera depois da primeira vez




"""

cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los angeles', 26)]

print(cidades)

# f = 9/5 * c + 32

# Lambda

c_para_f = lambda dado: (dado[0],(9/5) * dado[1] + 32)

print(list(map(c_para_f, cidades)))