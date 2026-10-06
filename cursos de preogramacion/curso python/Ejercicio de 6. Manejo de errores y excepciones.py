# Ejercicio propio: identificar errores comunes
errores = {
    "NameError": lambda: variable_inexistente,
    "TypeError": lambda: "edad: " + 30,
    "IndexError": lambda: [1, 2][5],
    "KeyError": lambda: {"a": 1}["b"],
    "ValueError": lambda: int("abc"),
}

for nombre, accion in errores.items():
    try:
        accion()
    except Exception as e:
        print(f"{nombre} -> {type(e).__name__}: {e}")
