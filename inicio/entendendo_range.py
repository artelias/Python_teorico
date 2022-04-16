"""
ranges

- Precisamos conhecer o loop for para usar os ranges.
- Precisamos conhecer range para trabalhar melhor com loops for.

Ranges são utilizados para gerar sequencias numericas, de maneira especificada pelo usuario.

Formas gerais:
range(valor_de_parada)

OBS: valor_de_paradanão nclusive (início padrão 0, e passo de 1 em 1)
#forma 1
for num in range(11):
    print(num)

#forma 2
range(valor_inicio,valor_final)
OBS:valor final não inclusivo

#exemplo forma 2
for num in range(4,11):
    print(num)

#forma 3
range(valor incial, valor final, passos)
OBS:valor final não incluido

#exemplo forma 3
for num in range(5,50,5):
    print(num)

#forma 4(inversa da forma 3, decrecente)
range(valor inicio, valor de parada, passos)
OBS:valor parada não incluido

#exemplo forma 4
for num in range(10, 0, -1):
    print(num)
"""
