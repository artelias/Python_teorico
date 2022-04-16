"""
maximo e minimo
max() retorna o maior e valor


"""
lista= {1, 8, 4, 99, 34, 129}
print(max(lista))
#Usando sorted para coisa mais complexas

musicas = [
    {"titulo": "thunderstruck", "tocou": 3},
    {"titulo": "flores", "tocou": 2},
    {"titulo": "back in black", "tocou": 4},
    {"titulo": "classic", "tocou": 32}
]

print(max(musicas, key=lambda musica: musica['tocou'])["titulo"])