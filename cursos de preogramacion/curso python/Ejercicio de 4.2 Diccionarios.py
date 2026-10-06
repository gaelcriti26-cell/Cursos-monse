# Ejercicio propio: diccionarios
# Inventario sencillo de una tienda.

inventario = {"manzanas": 10, "peras": 5}
inventario["uvas"] = 8
inventario.update({"peras": 7})

for producto, cantidad in inventario.items():
    print(f"{producto}: {cantidad} unidades")

print("Total de unidades:", sum(inventario.values()))
