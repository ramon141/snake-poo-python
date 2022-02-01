import Snake


class Playfield:
    def __init__(self, altura, largura):
        self.matriz = []
        self.snake = Snake.Snake(altura, largura)
        self.playfield = altura
        self.largura = largura

    def __str__(self):
        cobraStr = str(self.snake)
        return ("Altura = {0.altura}, Largura = {0.largura}, Cobra = [{1}]").format(self, cobraStr)
