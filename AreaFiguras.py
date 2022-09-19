import math


def calcularCuadrado(a):
    return a*a


def calcularAreaTriangulo(base, altura):
    return (base * altura)/2


def calcularAreaCirculo(radio):
    return math.pi * (radio*radio)


# Calculo del cuadrado
ladoCuadrado = int(input("Ingrese la medida de un lado del cuadrado:\n"))

print("El area es: ", calcularCuadrado(ladoCuadrado))
# Calculo del triangulo
base = int(input("\nIngrese la base del triangulo\n"))
altura = int(input("Ingrese la altura del triangulo\n"))

print("El area del triangulo es: ", calcularAreaTriangulo(base, altura))
# Calculo del circulo
radio = int(input("\nIngrese el radio del triangulo\n"))

print("El area del circulo es: ", calcularAreaCirculo(radio))
