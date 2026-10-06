# Ejercicio propio: guarda una lista de compras y léela línea a línea
compras = ["leche", "pan", "huevos"]

with open("compras.txt", "w", encoding="utf-8") as f:
    for item in compras:
        f.write(item + "\n")

with open("compras.txt", "r", encoding="utf-8") as f:
    for numero, linea in enumerate(f, start=1):
        print(numero, linea.strip())
