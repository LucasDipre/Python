class Livro:
    def __init__(self, titulo, autor, data_de_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.data_de_publicacao = data_de_publicacao


class Livro:
    def __init__(self, titulo, autor, preco, estoque):
        self.titulo = titulo
        self.autor = autor
        self.preco = preco
        self.estoque = estoque

livro = Livro("Python: Entendendo a Orientação a Objetos", "Nico Steppat", 49.90, 10)