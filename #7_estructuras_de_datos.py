# Estructuras de datos
"""
Las estructuras de datos nos permiten organizar y almacenar datos de manera eficiente en nuestros programas.
Python proporciona varias estructuras de datos integradas; como 'listas, tuplas, diccionarios y conjuntos', cada una con sus propias características y usos. 
"""

# Listas
"""
Una lista es una estructura de datos mutable y ordenada que permite almacenar una colección de elementos. Los elementos de una lista pueden ser de diferentes tipos de datos y se encierran entre corchetes '[]', separados sus elementos por comas ','
"""

# Creación y acceso
# Para crear una lista, simplemente encierra los elementos entre corchetes:

frutas = ["Manzana", "Banana", "Naranja"]
# Para acceder a los elementos de una lista, utiliza el índice del elemento entre corchetes. Recuerda: Los índices comienzan desde el 0.
print("Ejemplo de 'listas':")
print(frutas[0]) # muestra "Manzana"
print(frutas[1]) # muestra "Banana"
print(frutas[2]) # muestra "Naranja"

# También puedes acceder a los elementos desde el final de la lista utilizando índices negativos. El índice -1 representa el último elemento, -2 representa el penúltimo, y así sucesivamente...
print("_________________") # Esto es solo para separar del ejemplo anterior
print("Ejemplo de 'listas' con indices negativos:")
print(frutas[-1])  # Imprime "naranja"
print(frutas[-2])  # Imprime "banana"
print(frutas[-3])  # Imprime "manzana"

# Métodos de listas
"""
Las listas en Python tienen varios métodos incorporados que nos permiten manipular y modificar los elementos de la lista.
Algunos métodos comunes son:

    * append(elemento): Agrega un elemento al final de la lista.
    * insert(indice, elemento): Inserta un elemento en una posición específica de la lista.
    * remove(elemento): Elimina la primera aparición de un elemento en la lista.
    * pop(indice): Elimina y devuelve el elemento en una posición específica de la lista.
    * sort(): Ordena los elementos de la lista en orden ascendente.
    * reverse(): Invierte el orden de los elementos en la lista.
"""
# Ejemplos: