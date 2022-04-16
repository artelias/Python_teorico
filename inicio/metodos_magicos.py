"""
POO - Metodos magicos

Metodos Magicos, sao todos os metodos que utilizam dunder.

dunder initi -> ___init__()

Dunder -> Double Uderscore

# dunder repr -> Representacao do objeto
def __repr__(self):
    return f'{self.titulo} escrito por {self.autor}'


"""

class Livro:

    def __init__(self,titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __repr__(self):
        return f'{self.titulo} escrito por {self.autor}'
livro1 = Livro('Python RRocks!', 'Geek Univeersity', 400)
livro2 = Livro('IA com Python ', 'Geek Univeersity', 350)

print(str(livro1))
print(livro2)

