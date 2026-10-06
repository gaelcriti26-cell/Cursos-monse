# Ejercicio propio: división segura
def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("No se puede dividir entre cero")
    except TypeError:
        print("Solo se permiten números")
    finally:
        print("Operación terminada")

print(dividir(10, 2))
print(dividir(5, 0))
print(dividir("5", 1))
