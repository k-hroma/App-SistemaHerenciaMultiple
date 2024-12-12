from figura_geometrica import FiguraGeometrica
from color import Color


class Rectangulo(FiguraGeometrica, Color):
    contador_rectangulo = 0

    def __init__(self, ancho, alto, color):

        FiguraGeometrica.__init__(self, ancho, alto)

        Color.__init__(self, color)

    def __str__(self):
        return f"""
        Ancho: {self.ancho}
        Alto: {self.alto}
        Color: {self.color}
        """

    def calcular_area(self):
        Rectangulo.contador_rectangulo += 1
        id_rectangulo = Rectangulo.contador_rectangulo
        return f" Área del rectangulo n° {id_rectangulo}: {self.alto * self.ancho}"


if __name__ == "__main__":

    rectangulo1 = Rectangulo(2, 5, "rojo")
    print(rectangulo1)
    print(rectangulo1.calcular_area())
    rectangulo1.color = "verde"
    rectangulo1.alto = 4
    rectangulo1.ancho = 1
    print(rectangulo1)
    print(rectangulo1.calcular_area())
