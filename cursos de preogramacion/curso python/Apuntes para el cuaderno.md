# Apuntes para el cuaderno - Curso de Python

Sugerencia: una hoja (o media) por tema. Copia lo que está en **negrita** como títulos y escribe los ejemplos a mano; escribirlos ayuda a recordarlos.

---

## Hoja 1 - Primer programa
- **Título:** Mi primer programa
- Escribir: `print("¡Hola, Mundo!")` → muestra texto en pantalla
- Reglas: la **sangría** define los bloques · `#` comentario de una línea · `""" """` comentario de varias líneas · `;` separa instrucciones en una línea
- Dibuja: un `if` con su bloque sangrado, marcando con una flecha dónde empieza el bloque

## Hoja 2 - Variables
- **Título:** Variables
- Definición (con tus palabras): etiqueta que guarda un valor
- Ejemplo: `nombre = "Juan"` `edad = 25` `altura = 1.75` `es_estudiante = True`
- Tabla de tipos: `str` texto · `int` entero · `float` decimal · `bool` True/False
- Reglas de nombres: ✔ `total_ventas`, `_contador` · ✘ `1edad`, `nombre-completo`, `if`
- Asignación múltiple: `a = b = c = 10`

## Hoja 3 - Operadores
- **Título:** Operadores (haz tres columnas)
  - Aritméticos: `+ - * / // % **` con `a=10, b=3` → 13, 7, 30, 3.33, 3, 1, 1000
  - Comparación: `== != > < >= <=` → devuelven True/False
  - Lógicos: `and`, `or`, `not`
- Recuadro de alerta: `=` asigna · `==` compara

## Hoja 4 - Condicionales
- **Título:** if / elif / else
- Esquema:
  ```
  if condicion1:
      ...
  elif condicion2:
      ...
  else:
      ...
  ```
- Ejemplo de calificaciones (≥90 Excelente, ≥80 Muy bueno, ≥70 Bueno, si no Necesita mejorar)
- Nota: solo se ejecuta el primer bloque verdadero

## Hoja 5 - Bucles
- **Título:** for y while
- `for fruta in frutas:` → recorre una secuencia · `range(10)` → 0 a 9
- `while contador < 5:` → repite mientras sea verdadero (¡actualiza el contador!)
- Tabla: `break` sale · `continue` salta a la siguiente vuelta · `pass` no hace nada

## Hoja 6 - Listas
- **Título:** Listas `[ ]` (ordenadas, modificables)
- Dibuja la lista `["manzana", "banana", "naranja"]` con los índices 0, 1, 2 arriba y -3, -2, -1 abajo
- Métodos (tabla): `append` agrega al final · `insert(i, x)` agrega en posición · `remove(x)` borra por valor · `pop(i)` borra por posición y la devuelve · `sort()` ordena · `reverse()` invierte
- Comprensión de listas: `[x ** 2 for x in numeros if x % 2 == 0]` → `[4, 16]`

## Hoja 7 - Tuplas, diccionarios y sets
- **Título:** Comparativa de estructuras (haz la tabla)

  | | Lista | Tupla | Diccionario | Set |
  |---|---|---|---|---|
  | Símbolo | `[ ]` | `( )` | `{clave: valor}` | `{ }` |
  | Modificable | Sí | No | Sí | Sí |
  | Duplicados | Sí | Sí | Claves únicas | No |

- Tuplas: `punto = (3, 4)` · `index(valor, inicio, fin)`
- Diccionarios: `persona["nombre"]` · `keys()` `values()` `items()` `update()`
- Sets: diagrama de Venn con `|` unión, `&` intersección, `-` diferencia, `^` simétrica (usa `{1,2,3}` y `{3,4,5}`)
- Sets: `add`, `remove` (error si no existe), `discard` (sin error), `clear`

## Hoja 8 - Funciones
- **Título:** Funciones
- Esquema: `def nombre(parametros):` + cuerpo sangrado + `return`
- Ejemplos: `def suma(a, b): return a + b` · `lambda x: x ** 2`
- Recuadro: **local** (dentro de la función) vs **global** (fuera)
- Docstring: `""" descripción, Args, Returns """`
- `*numeros` → número variable de argumentos

## Hoja 9 - Errores y excepciones
- **Título:** Errores comunes (tabla: error / cuándo ocurre / ejemplo)
  - `SyntaxError` · falta un `:` · `def f()`
  - `NameError` · variable no definida
  - `TypeError` · tipos incompatibles · `5 + "10"`
  - `IndexError` · índice fuera de rango · `lista[3]`
- Esquema:
  ```
  try:
      ...código que puede fallar
  except TipoError:
      ...qué hacer
  finally:
      ...siempre se ejecuta
  ```
- Excepciones propias: `raise Exception("mensaje")` y `except Exception as e:`

## Hoja 10 - Entradas y salidas
- **Título:** input, f-strings y archivos
- `input()` → siempre devuelve texto → convertir: `int(input("Edad: "))`
- f-string: `f"Hola, {nombre}"`
- Tabla de archivos: `"r"` leer · `"w"` escribir (sobrescribe) · `read()` · `write()` · `close()`
- Recuadro destacado: `with open("datos.txt", "r") as archivo:` → se cierra solo

## Hoja 11 - Módulos y paquetes
- **Título:** Importar código
- `import math` → `math.sqrt(25)` · `from math import sqrt` → `sqrt(25)`
- Biblioteca estándar: `math`, `random`, `datetime`
- Módulo propio = archivo `.py` → `import mi_modulo`
- Dibuja el árbol de un paquete:
  ```
  mi_paquete/
      __init__.py
      modulo1.py
      modulo2.py
  ```
- `from mi_paquete import modulo1, modulo2`

## Hoja final - Resumen en una página
- Los 4 tipos de datos básicos, los 3 grupos de operadores y la tabla de estructuras de datos
- Plantillas de `if`, `for`, `while`, `def` y `try/except`
- Tus 5 errores más frecuentes (anótalos mientras practicas)

---

## Consejos para el cuaderno
- Usa **un color** para títulos, otro para código y otro para advertencias.
- Deja una columna al margen para dudas y márcalas para revisarlas después.
- Anota siempre qué **imprime** cada ejemplo, no solo el código.
- Al final de cada hoja escribe una frase: "Esto sirve para...".
