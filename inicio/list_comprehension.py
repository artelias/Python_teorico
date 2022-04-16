"""
List comprehension
- utilizando list comprehension nós podemos gerar novas listas com dados processados a partir de outro iterável.

# Sintaxe da List comprehension

[ dado for in iterável ]

# Exemplo
numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]
print(res)

Para entender melhor o que está acontecendo devemos divir a expressão em duas partes:

- A primeira parte: for numero in numeros
- A segunda parte: numero * 10
res = [numero / 2 for numero in numeros]

print(res)


#List Comprehension versos Loop

#Loop
numeros = [1 ,2, 3, 4, 5]
numeros_dobrados = []

for numero in numeros:
    numero_dobrado = numero * 2
    numeros_dobrados.append(numero_dobrado)

print(numeros_dobrados)

#list comprehension
print([numero *2 for numero in numeros])

# Outros exemplos
#1

nomes = 'arthur'

print(([letra.upper() for letra in nomes]))

# 2
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

print(pares)
print(impares)

# refatorar

# Qualquer nímero par módulo de 2 é 0 e 0 em python é False. not False = True
pares = [numero for numero in numeros if not numero % 2]
# qualquer número impar módulo de 2 é 1, ou seja, True

impares = [numero for numero in numeros if numero % 2]

print(pares)
print(impares)

# 3
res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)


"""
