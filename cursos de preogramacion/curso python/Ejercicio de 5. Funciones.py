# Ejercicio propio: funciones
# Calcula el promedio y decide si es aprobatorio.

def promedio(*notas):
    """Devuelve el promedio de las notas recibidas."""
    return sum(notas) / len(notas)

def aprobado(nota, minimo=60):
    return nota >= minimo

media = promedio(70, 55, 90)
print("Promedio:", media)
print("¿Aprobado?", aprobado(media))

doble = lambda x: x * 2
print("Doble de 8:", doble(8))
