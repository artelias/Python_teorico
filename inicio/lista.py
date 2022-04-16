"""
Listas

Listas em python funcionam como vetores ou matrizes (arrays) em outras linguagens, com  a diferença de serem dinamicos
e também de podermos coloca qualuqer tipo de dado.

Listas são mutaveis: ou seja pode mudar constantemente.

Linguagens C/Java: Arrays
    - Possuem tamanho e tipo de dado fixo:
    ou seja, nestas linguagens se você criar um array do tipo int e com tamanho 5, este array
    será sempre do tipo inteiro e poderá ter sempre no máximo 5 valores

Já em Python:

- Dinâmico: Não possui tamanho fixo; Ou seja, podemos criar a lista e simplesmente ir adicionando elementos;
- Qualquer tipo de dado: não possuem tipo de dado fixo; Ou seja, podemos colocar qualuqer tipo de dado;
As listas em python são representada por []



"""
"""
lista1 = [1, 99, 23, 55, 66, 77, 33, 1, 44, 43, 26]
lista2 = ['G', 'E', 'E', 'K', '', 'U', 'N', 'I', 'V', 'E', 'R', 'S', 'I', 'T', 'Y']
lista3 = []
lista4 = list(range(11))
lista5 = list('Geek Uniersity')

# podemos facilmente checar se o valor esta na lista
if 8 in lista4:
    print('Encontrei o numero 8')
else:
    print('n encontrei')
# podemos facilmente ordenar uma lista
lista1.sort()
print(lista1)
# Pdemos facilmente contar o número de ocorrências de um valor em uma lista
print(lista1.count(1))
print(lista5.count('e'))


#Podemos adiciona elementos em listas, usando o comando append

lista1.append([8, 3, 1])#coloca como elemento unico, ou seja, sublista
print(lista1)
if [8, 3, 1] in lista1:
    print('Encontrei a lista')
else:
    print('não encontrei a lista')
lista1.extend([123, 44, 66])#coloca cada elemento individualmente
print(lista1)

# podemos insirir um novo elemento na lista informando a posição do indice
# OBS: Isso não substitui o valor inicial. o mesmo será deslocado para a direita da lista.
lista1.insert(2, 'novo valor')
print(lista1)

#facilmente podemos unir as listas
lista6 = lista1 + lista2
#ou se quiser unir em uma lista já criada 
lista1.extend(lista2)


#podemos facilente inverte uma lista
lista1.reverse()
#ou
print(lista1[::-1])

#quantos elementos existem dentro da lista
print(len(lista1))

#podemos remover facilmente o ultimo elemento de uma lista ou qualquer outro se for inserido
lista5.pop()

#podemos remover toda lista
lista5.clear()

#convertendo uma string em uma lista
#exemplo 1
curso = 'programação em Python: Essencial'
print(curso)
curso = curso.split()
print(curso)

#Por definição o split separa os elementos da lista pelo espaço entre elas.

#Exemplo 2
curso = 'programação,em,Python:,Essencial'
print(curso)
curso = curso.split(',')
print(curso)
#SEU SEPARADOR MUDOU PARA ,

#convertendo ums lista em string

lista6 = ['Programação', 'em', 'Python:', 'Essencial']
print(lista6)
#abaixo estamos falando: 'pega a lista6 e coloca espaço entre cada elemento e transforma em uma string
curso = ' '.join(lista6)
print(curso)

curso = 'progrmação$em$Python:$Essencial'
curso = curso.split('$')
print(curso)

#utilizando while

carrinho = []
produtor = ''

while produtor != 'sair':
    print("adicione um produto na lista ou digite 'sair' para sair: ")
    produtor = input()
    if produtor != 'sair':
        carrinho.append(produtor)
for produtor in carrinho:
    print(produtor)
    
    cores = ['verde', 'amarelo', 'azul', 'branco']

for cor in cores:
    print(cor)
indice = 0
while indice < len(cores):
    print(cores[indice])
    indice= indice + 1

for indice, cor in enumerate(cores):
    print(indice, cor)
    
numeros = [5, 6, 7, 5, 8, 9, 10]
#em qual indice está o valor 9
print(numeros.index(9))
#OBS: irá mostra o primeiro valor encontrado
print(numeros.index(5))

#podemos fazer busca dentro de um range, inicio /fim
print(numeros.index(8, 3, 6))# procura o valor 8 entre o indice 3 e 6

# Revisão de slicing

# lista(inicio:fim:passos)
#range(inicio:fim:passos)

#trabalho com slice de lista com o parâmetro 'inicio'

lista = [1, 2, 3, 4]

print(lista[0:3])

#invertendo valores em uma lista

nomes = ['Geek', 'University']
nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)
# ou usar
nomes = ['Geek', 'University']
nomes.reverse()
print(nomes)

print(sum(lista))#soma os valores da lista
print(max(lista))# valor maximo da lista
print(min(lista))#valor minimo da lista
print(len(lista))#tamanho da lista
"""

#transforma uma lista em tupla
lista = [1, 2, 3, 4, 5 ,6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))