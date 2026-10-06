# Ejercicio propio: conjuntos
# Elimina duplicados y compara dos grupos de personas.

asistentes = ["Ana", "Luis", "Ana", "Eva", "Luis"]
unicos = set(asistentes)
print("Asistentes únicos:", unicos)

grupo_a = {"Ana", "Luis", "Eva"}
grupo_b = {"Eva", "Marta"}
print("En ambos grupos:", grupo_a & grupo_b)
print("Solo en A:", grupo_a - grupo_b)
print("Todos:", grupo_a | grupo_b)
