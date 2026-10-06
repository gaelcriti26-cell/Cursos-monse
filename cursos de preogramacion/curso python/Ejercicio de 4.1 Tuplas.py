# Ejercicio propio: tuplas
# Las tuplas son inmutables: guardan coordenadas y se desempaquetan.

coordenada = (10.5, 20.3)
x, y = coordenada
print("x =", x, "| y =", y)
print("Cantidad de elementos:", len(coordenada))

try:
    coordenada[0] = 99
except TypeError as e:
    print("Error esperado, las tuplas no se modifican:", e)
