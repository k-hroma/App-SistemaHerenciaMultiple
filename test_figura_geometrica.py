from cuadrado import Cuadrado
from rectangulo import Rectangulo

while True:

    ancho = int(input("Ingrese valor: "))
    alto = int(input("Ingrese valor: "))
    color = input("Ingrese color: ")

    if alto == ancho:
        cuadrado = Cuadrado(ancho, alto, color)
        print(cuadrado)
        print(cuadrado.calcular_area())

    elif alto != ancho:
        rectangulo = Rectangulo(ancho, alto, color)
        print(rectangulo)
        print(rectangulo.calcular_area())

    else:
        False
