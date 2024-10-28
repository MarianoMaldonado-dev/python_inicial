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
frutas1 = ["manzana", "banana", "naranja"]
frutas1.append("pera")
print("_________________") # Esto es solo para separar del ejemplo anterior
print("Ejemplo de 'listas' con métodos: 'append()':")
print(frutas1) #Veremos que se agrega Pera al final de la lista

frutas1.insert(1, "uva")
print("_________________") # Esto es solo para separar del ejemplo anterior
print("Ejemplo de 'listas' con métodos: 'insert()':")
print(frutas1) # Veremos que 'uva' se agrega a la lista en el indice 1

frutas1.remove("banana")
print("_________________") # Esto es solo para separar del ejemplo anterior
print("Ejemplo de 'listas' con métodos: 'remove()':")
print(frutas1)

fruta_podrida = frutas1.pop(2)
print("_________________") # Esto es solo para separar del ejemplo anterior
print("Ejemplo de 'listas' con métodos: 'pop()':")
print(frutas1)
print(fruta_podrida) # Nos mostrará la fruta que fue eliminada de la lista

frutas1.sort()
print("_________________") # Esto es solo para separar del ejemplo anterior
print("Ejemplo de 'listas' con métodos: 'sort()':")
print(frutas1)

frutas1.reverse()
print("_________________") # Esto es solo para separar del ejemplo anterior
print("Ejemplo de 'listas' con métodos: 'reverse()':")
print(frutas1) # Nos devolverá el orden de la lista al revés

# Listas de comprensión
"""
Las listas de comprensión son una forma concisa de crear nuevas listas basadas
en una secuencia existente. Permiten filtrar y transformar
los elementos de una lista en una sola línea de código.
La sintaxis es la siguiente:
"""
# lista_de_comprension = ['expresion' for 'elemento' in 'secuencia' if 'condicion']
# Ejemplo:
print("_________________") # Esto es solo para separar del ejemplo anterior
print("Ejemplo de 'listas de comprensión:")
nums = [1, 2, 3, 4, 5]
cuadrados = [x**2 for x in nums if x % 2 == 0]
print(cuadrados) #Nos mostrará [4, 16]
"""
En éste ejemplo, se crea una nueva lista llamada cuadrados, que contiene los cuadrados de los números 
pares de la lista números. La expresión x**2 eleva cada elemento
al cuadrado, y la condición 'if x % 2 == 0' filtra solo los números pares.
"""

# Tuplas
"""
Una tupla es una estructura de datos inmutable y ordenada que permite almacenar
una colección de elementos. Los elementos de una tupla se encierran entre paréntesis
y separados por coma.
"""
# Creación y acceso
# Para crear una tupla, encierra los elementos entre paréntesis:
punto = (3, 4)
# Para acceder a los elementos de una tupla, utiliza el índice del elemento entre corchetes, similar a las listas:
print(punto[0]) #Nos muestra el 3
print(punto[1]) #Nos muestra el 4
"""
A diferencia de las listas, las tuplas son inmutables, lo que significa que no se pueden modificar una vez creadas.
No se pueden agregar, eliminar o cambiar elementos en una tupla existente.

Las tuplas son útiles cuando necesitas almacenar una colección de elementos que no deben modificarse,
como coordenadas o datos de configuración
"""

# Métodos de tuplas
# Aunque las tuplas son inmutables, python proporciona varios métodos útiles para trabajar con ellas:
"""
count(elemento): devuelve el número de veces que aparece un elemento en la tupla.

index(elemento): devuelve el índice de la primera aparición de un elemento en la tupla.
Opcionalmente, se puede especificar el inicio y fin de la búsqueda.

len(tupla): aunque no es un método de tupla propiamente dicho, esta función incorporada devuelve la longitud de la tupla.
"""
tupla1 = (1, 2, 3, 2, 4, 2)
print("_________________") # Esto es solo para separar del ejemplo anterior
print("Ejemplo de 'tupla' con métodos: 'index()':")

print(tupla1.index(2)) #Mostrará 1
print(tupla1.index(2, 2)) #Mostrará 3
print(tupla1.index(2, 2, 4)) #Mostrará 3