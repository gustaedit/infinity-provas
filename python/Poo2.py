""" Imagine que você está desenvolvendo um sistema para gerenciar uma biblioteca. 

Nessa biblioteca, existem diferentes tipos de livros, como romances, biografias, livros infantis, etc. 

Todos esses livros possuem algumas características em comum, como o título, o autor e a editora, mas também possuem características específicas,

como o número de páginas, a faixa etária recomendada, etc.


O exercício consiste em implementar as classes Livro,
 Romance e Biografia, de forma que a classe Livro seja a super classe e contenha as características em comum. 
 As classes Romance e Biografia devem herdar da classe Livro e adicionar as características específicas de cada tipo de livro.
   Também é necessário implementar o método exibir_detalhes() em cada classe, que deve exibir as características específicas do livro

   sua resposra:"""
class Livro:
    def __init__(self, titulo, autor, editora, numero_de_paginas):
        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.numero_de_paginas = numero_de_paginas
    
    def exibir_detalhes(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Editora: {self.editora}")
        print(f"Número de Páginas: {self.numero_de_paginas}")

class Romance(Livro):
    def __init__(self, titulo, autor, editora, numero_de_paginas, faixa_etaria):
        super().__init__(titulo, autor, editora, numero_de_paginas)
        self.faixa_etaria = faixa_etaria
    
    def exibir_detalhes(self):
        super().exibir_detalhes()
        print(f"Faixa Etária Recomendada: {self.faixa_etaria}")

class Biografia(Livro):
    def __init__(self, titulo, autor, editora, numero_de_paginas, biografado):
        super().__init__(titulo, autor, editora, numero_de_paginas)
        self.biografado = biografado
    
    def exibir_detalhes(self):
        super().exibir_detalhes()
        print(f"Biografado: {self.biografado}")

livro_romance = Romance("Amor Proibido", "Maria Silva", "Editora ABC", 300, "16+")
livro_biografia = Biografia("Steve Jobs: A Biografia", "Walter Isaacson", "Companhia das Letras", 600, "Steve Jobs")

print("Detalhes do Romance:")
livro_romance.exibir_detalhes()

print("\nDetalhes da Biografia:")
livro_biografia.exibir_detalhes()
