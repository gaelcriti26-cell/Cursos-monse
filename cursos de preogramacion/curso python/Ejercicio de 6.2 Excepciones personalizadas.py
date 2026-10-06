# Ejercicio propio: excepción propia para validar edad
class EdadInvalidaError(Exception):
    """Se lanza cuando la edad no es válida."""

def registrar(edad):
    if edad < 0 or edad > 120:
        raise EdadInvalidaError(f"Edad inválida: {edad}")
    print("Edad registrada:", edad)

for valor in (25, -3):
    try:
        registrar(valor)
    except EdadInvalidaError as e:
        print("Error:", e)
