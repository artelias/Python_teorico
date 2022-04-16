"""
loop while

forma geral
while: expressão bulooleana:
    //execução do loop

o bloco do while será repetido enquanto a expressão booleana for verdadeira.

Expressão booleana é toda expressão em que o resultado é verdadeiro ou falso.
exemplo
num=5
num<5
false

numero=1
while numero < 10:
    print(numero)
    numero = numero + 1
#OBS: em um lopp while é importante que cuidemos do criterio de parada. ou seja o ponto que vc quer seja falso. só para se for falso.

"""

resposta = ''
while resposta != 'sim':
    resposta = input('já acabou jessica?')

