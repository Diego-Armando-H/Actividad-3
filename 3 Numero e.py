def factorial(n):
    fac = 1
    for i in range(1, n+1):
        fac = fac * i
    return fac


print("Calculando e:\n")
limite = int(input("Ingrese un limite entero:\n"))
# Inicializamos los valores para el calculo
n = 0
e = 0
while n < limite:
    e += 1/factorial(n)  # se llama a la función factorial creada por ti
    n = n + 1

print("Resultado del calculo: ", e)
