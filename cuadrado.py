from figura_geometrica import FiguraGeometrica
from color import Color


class Cuadrado(FiguraGeometrica, Color):
    contador_cuadrado = 0

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
        Cuadrado.contador_cuadrado += 1
        id_cuadrado = Cuadrado.contador_cuadrado
        return f" Área del cuadrado n° {id_cuadrado}: {self.alto * self.ancho}"


if __name__ == "__main__":

    cuadrado1 = Cuadrado(2, 2, "verde")
    print(cuadrado1)
    print(cuadrado1.calcular_area())
    cuadrado1.color = "azul"
    cuadrado1.alto = 1
    cuadrado1.ancho = 1
    print(cuadrado1)
    print(cuadrado1.calcular_area())