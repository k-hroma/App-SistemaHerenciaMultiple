class FiguraGeometrica:
    contador_figura_geometrica = 0

    def __init__(self, ancho, alto):
        self._ancho = ancho
        self._alto = alto

    def __str__(self):
        FiguraGeometrica.contador_figura_geometrica += 1
        id_fg = FiguraGeometrica.contador_figura_geometrica
        return f"""
        Figura Geometrica: {id_fg}
        Ancho: {self.ancho}
        Alto: {self.alto}"""  

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        self._ancho = ancho

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        self._alto = alto


if __name__ == "__main__":

    fg1 = FiguraGeometrica(2, 2)
    print(fg1)
    fg2 = FiguraGeometrica(3, 3)
    print(fg2)