"""
Dicionários

OBS: Em algumas linguagens de programação, os dicionários Pythom são conhecidos por mapas.

dicionários são coleções do tipo chave/ valor.

Dicionários são representados por chaves {}

print(type({}))

#criação de dicionários
paises = {'br': 'Brasil', 'EUA': 'Estados unidos', 'py': 'Paraguai'}
print(paises)
print(type(paises))

#acessando elementos

#forma 1- acessando via chave, da mesma forma que lista/tupla
print(paises['br'])

#forma 2- acessando via get- recomendado*
# * se n existir dará none
print(paises.get('br'))

#atualizar dados em um dicionário

# Forma 1
receira['mai']= 550
print(receita)

# Forma 2
receita.update({'mai':600})

print(receita)
#conclusão 1: A forma de adicionar novos elementos ou atualizar dados em um dicionário é a mesma.
# conclusão 2: Em dicionários, nâo podemos ter chaves repetidas.
"""
