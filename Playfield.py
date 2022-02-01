import Snake


class Playfield:
    def __init__(self, altura, largura):
        matriz = []

        for i in range(largura):
            listAltura = []
            for j in range(altura):
                listAltura.append(False)
            matriz.append(listAltura)

        self.matriz = matriz
        self.snake = Snake.Snake(altura, largura)
        self.playfield = altura
        self.largura = largura

    def __str__(self):
        string = "["
        for linha in self.matriz:
            string += "["
            for coluna in linha:
                string = ("{0}{1}, ").format(string, coluna)
            string = ("{0}]").format(string[0:len(string)-2])

        return string + "]"
