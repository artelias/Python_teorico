"""
Filter

filter() -> Serve pra filtra determinado dado




"""

import statistics

# dados coletados
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

#calculando a média dos dados utilizando mean()
media = statistics.mean(dados)

print(f'media: {media}')

res = filter(lambda valor: valor > media, dados)
print((list(res)))

print(f'novamente: {list(res)}')
