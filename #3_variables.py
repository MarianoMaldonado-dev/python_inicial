#Variables

"""
Las variables son contenedores que nos permiten almacenar y manipular datos en nuestros programas.
Puedes pensar en una variable como una etiqueta a la que asignas a un valor específico.
En python, no es necesario declarar el tipo de datos de una variable de antemano, 
ya que Python infiere el tipo de datos automáticamente en función del valor asignado.
"""

#Declaración y asignación de variables
"""
Para declarar y asignar un valor a una variable en Python, utilizamos el operador de asignacion  ' = '
El nombre de la variable va a la izquierda del operador, y el valor que deseas asignar va a la derecha.
Por ejemplo:
"""
nombre = "Fulano"
edad = 25
altura = 1.75
es_estudiante = True
"""
En el ejemplo, hemos declarado y asignado valores a las variables nombre, edad, altura y es_estudiante.
Python infiere automáticamente el tipo de datos de cada variable en función del valor asignado.
También puedes asignar el mismo valor a múltiples variables en una sola línea utilizando el operador de asignación múltiple:
"""
a = b = c = 10
#En éste caso, las variables a, b y c tendrán el valor 10

#Regla para nombrar variables
"""
Al nombrar variables en Python, es importante seguir algunas normas para mantener un código legible y evitar errores:

	1. Los nombres de las variables solo pueden contener letras (a-z, A-Z),
			números (0-9) y guiones bajos (_). No pueden comenzar con un número.
	2. No se pueden utilizar palabras clave reservadas de python como nombres
			de variables (por ejemplo: if, else, for, while, etc)
	3. Python distingue entre mayúsculas y minúsculas, por lo que nombre y Nombre son variables diferentes.
	4. Se recomienda utilizar nombres descriptivos para las variables, que indiquen claramente su propósito: nombre, edad, total_ventas, etc.
"""
#Siguiendo ésta regla, algunos ejemplos de nombres de variables válidos son:
edad
nombre_completo
total_ventas
_contador

#Ejemplos de Nombres de variables inválidos:
"""
1edad (Comienza con un número) 
nombre-completo (Utiliza un guión medio en lugar de un guión bajo)
if (Es una palabra clave reservada de Python)
"""
