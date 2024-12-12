class Color:
    contador_colores = 0

    def __init__(self, color):
        self._color = color

    def __str__(self):
        Color.contador_colores += 1
        id_color = Color.contador_colores
        return f" Color {id_color}: {self.color}"

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color


if __name__ == "__main__":

    color1 = Color("rojo")
    print(color1)
    color1.color = "blanco"
    print(color1)