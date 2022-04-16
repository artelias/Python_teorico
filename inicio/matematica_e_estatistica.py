import math

# math.prod - retorna o produto de um container numerico
nuns_v1 = [2,3,6,8]
nuns_v2 = (2,3,6,8)
nuns_v3 = {2,3,6,8}

print(math.prod(nuns_v1))
print(math.prod(nuns_v2))
print(math.prod(nuns_v3))

# math.isqrt

print(math.isqrt(9))
print(math.isqrt(17))
print(math.sqrt(9))
print(math.sqrt(17))

# math.dist - retorna a distancia euclidiana entre dois pontos, 3d ou 2d
#pontos 3D
p3d1 = (12,50,40)
p3d2 = (6,7,13)

# pontos 2D
p2d1 = [12, 50]
p2d2 = [6, 7]

print(math.dist(p3d1,p3d2))
print(math.dist(p2d1,p2d2))

######################## ESTATISTICA #############################

import statistics

valores_reais = [1.45,6.78,3.54,36.9]
valores_inteiros = [1,6,7,3,69]
# medias
print(statistics.fmean(valores_inteiros))
print(statistics.fmean(valores_reais))

print(statistics.geometric_mean(valores_reais))
print(statistics.geometric_mean(valores_inteiros))


# moda

seq1 = 'arthur henrique'
seq2 = [3,4,5,23,2,1,3,3,3]
seq3 = [1,1,1,3,3,3,4,4,4]
print(statistics.multimode(seq1))
print(statistics.multimode(seq2))
print(statistics.multimode(seq3))