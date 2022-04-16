"""
Sorted

#é um comando de ordenação da seguinte forma

# Exemplos

numeros = {6, 1, 8, 2}
print(numeros)

print(sorted((numeros))) #Ordenar do menor pro maior

print(numeros)

# Exemplos

numeros = {6, 1, 8, 2}
print(sorted(numeros))
# Adicionandoo parâmetros ao sorted()
print(sorted(numeros, reverse= True))



#Usando sorted para coisa mais complexas

musicas = [
    {"titulo": "thunderstruck", "tocou": 3},
    {"titulo": "flores", "tocou": 2},
    {"titulo": "back in black", "tocou": 4},
    {"titulo": "classic", "tocou": 32}
]

print(sorted(musicas, key=lambda musica: musica['tocou']))
"""

