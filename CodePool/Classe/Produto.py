class Produto:
    def __init__(self, titulo, categoria, preco, estoque):
        self.titulo = titulo
        self.categoria = categoria
        self.preco = preco
        self.estoque = estoque

produto = Produto("Ração para gatos premium", "Alimentos", 79.90, 25)