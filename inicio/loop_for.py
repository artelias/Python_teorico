"""
Loop for

Loop->Estrutura de repetição.
for -> Uma dessas estruturas.

C ou Java

for(int i = 0; i<10; i++){
    //execução do loop
}
Python
for item in interavel:
    // execução do loop

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis
Exemplo de interáveis:
- String
    nome = 'Geek University'
- Lista
    lista = [1, 3, 5, 7, 9]
- Range
   numeros = range(1,10)

"""
"""
nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)#temos que transforma em lista
#exemplo de for 1(iterando sobre uma string
for letra in nome:
    print(letra)

#exemplo de for 2(iterando sobre uma lista
for numero in lista:
    print(numero)

# Exemplo de for 3(iterando sobre uma range)
for numero in range(1, 10):
    print(numero)
#exemplo 4    
    
    for indice, letra in enumerate(nome):
    print(nome[indice])
#exemplo 5

for valor in enumerate(nome):
    print(valor)

#exemplo 6
qtd = int(input(' Quantas vezes esse loop deve rodar? '))
soma = 0
for n in range(1, qtd+1):
   num = int(input(f'Informe o {n}/{qtd}  valor: '))
   soma = soma + num
print(f'A soma é {soma}')
"""

#U+1F60D

for num in range(1, 11):
    print('\U0001F60D' * num)