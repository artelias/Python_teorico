"""
Funções com parâmetro(de entrada)
- Funções que recebem dados para serem processados dentro da mesma;

Se a gente pensar em um programa qualquer, geralmente temos:
entrada -> processamento -> saída

Se a gente pensar em uma função, já sabemos que temos funções que:
- Não possuem entrada;
- não possuem saída
- Possuem entrada, mas não possuem saída;
- Não possuem entrada, mas possuem saída;
- Possuem entrada e possuem saída

# exemplo 1
def quadrado(numero):
    return numero * numero


print(quadrado(7))


# EXEMPLO 2

def tabuada(numero):
    if numero:
        n = range(11)
        multiplo = n * numero
        return multiplo



print(tabuada(1))


# exemplo 3
def multiplicar(num1, num2):
    return num1 * num2

print(multiplicar(2, 3))
"""




# exemplo 4
def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0: # modulo de num dividido por 2
            total = total + num
    return total

if __name__ == '__main__':
    lista = [1, 2, 3, 4 ,5, 6, 7]
    print(soma_impares(lista))