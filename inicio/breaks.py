""""
Saindo de loop com breaks

Funciona da mesma forma que nas linguagens C ou Java.

Utilizamos o break para sair de loops de maneira forçada ou projetada.

#exemplo 1
for numero in range(1,11):
    if numero == 6:
        break
    else:
        print(numero)
print('sair do loop')

#exemplo 2
while True:
    comando = input("digite 'sair' para sair: ")
    if comando == 'sair':
        break
"""
