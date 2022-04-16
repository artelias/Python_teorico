"""
Definindo funções

- funções são pequenos trechos de código que realizam tarefas específicas;
- Pode ou não receber entradas de dados e retornar uma saída de dados;
- Muito uteis para executar procedimentos similares por repetidas vezes;

OBS: Se você escrever uma fução que realiza várias tarefas dentro dela;
é bom fazer uma verificação para que a função seja simplificada.

Já usamos as seguintes funções
* print()
* len()
* max()
* min()
* count
e muitas outras
"""

# Exemplo de utilização de funções:

cores = ['verde', 'amarelo', 'azul', 'branco']

# utilizando a função integrada (Built-in) do Python print()
print(cores)

# função de adição de objeto dentro de uma variavel já criada, lista, tuplas conjuntos...
cores.append('roxo')

# função que limpa seu objeto(lista...)
cores.clear()  # sem parametro

# mas como definir funções a minha escolha???

"""
Em Python, a forma geral de definir uma função é:

def nome_dafuncao(parametros_de_entrada):
     bloco_da_funcao

onde:
nome_da_função -> SEMPRE, em minusculo, se quiser separar é _
parametros_de_entrada -> Opcionais, separados por virgulas
bloco_da_funcao -> Também chamado de corpo da função ou implementação, é onde

"""


# Definindo a primeira função

def diz_oi():
    print('OI')

"""
OBS: essa função é do tipo void, ou seja, não retorna nada.
- não recebe nenhum parametro de entrada
"""

#exemplo 2
def cantar_parabens():
    print('parabens pra você')
    print('nesta data querida')
    print('muitos anos de vida')
    print('muitas felicidades, muitos anos de vida')

#Em Python, podemos inclusive criar variáveis do tipo de uma função e executar esta função através da variável
#canta = cantar_parabens()
#canta
