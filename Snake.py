class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tamanho = 1
        self.direcao = 0
        pass

    def __str__(self):
        lista = ["Parada", "Direita", "Esquerda", "Cima", "Baixo"]
        direcao = lista[self.direcao]
        return ("Tamanho = {0.tamanho} -- Ponto = ({0.x}, {0.y}) -- Direcao = {1}").format(self, direcao)
