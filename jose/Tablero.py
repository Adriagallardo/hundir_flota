class Tablero:

    def __init__(self, altura, anchura):
        self.altura = altura
        self.anchura = anchura
        self.tabla = [[str(x) if y == 0 else str(y) if x == 0 else '~' for x in range(self.anchura + 1)] for y in range(self.altura + 1)]

    def mostrar_pantalla(self):
        for i in range(self.altura + 1):
            print(' '.join(self.tabla[i]))
        