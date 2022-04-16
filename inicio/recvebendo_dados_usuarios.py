"""
recebendo dados do usuário
input() -> todo dado recebido via input é do tipo string
Em Python, string é tudo qie estiver entre
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;
exemplos
- Aspas somples -> 'arthur'
- Aspas duplas -> "arthur"
- Aspas simples triplas -> '''arthur'''
- Aspas duplas tripla ->"""arthur"""
"""
"""
usado sem formatação
# entrada de dados
print("qual seu nome?")
nome = input()  # imput->entrada
print('qual sua idade?')
idade = input()

# processamento


# saída de dados
print('seja bem-vindo(a)%s com %s anos'  % (nome, idade))
"""
#utilizando formatação atual do python
print('qual seu nome?')
nome = input()
print(f'seja bem-vindo(a) {nome}')

print("qual sua idade? ")
idade = input()

print(f'seu nome é {nome} e você tem {idade} anos, então seja muito bem-vindo')
"""
#int(idade) => cast
cast é a 'conversão de um tipo de dado para outro.
"""
print(f'A {nome} nasceu em {2018  - int(idade)}')