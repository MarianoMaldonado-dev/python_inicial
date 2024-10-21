# Estructuras de control
"""
Las estructuras de control nos permiten controlar el flujo de ejecución de nuestros programas.
En python, las estructuras de control más comunes son las estructuras condicionales y los bucles.
Estas estructuras nos permiten tomar decisiones y repetir bloques de código según ciertas condiciones.
"""

# Estructuras condicionales
"""
Las estructuras condicionales nos permiten ejecutar diferentes bloques de código según se cumpla o no
una determinada condición. En python, las estructuras condicionales más utilizadas son:
if, if-else y if-elif-else
"""

# if
"""
 La estructura if se utiliza pra ejecutar un bloqe de código si una condición es verdadera.
 Su sintaxis es la siguiente:
 """
 # if condicion:
			# Aquí va el código a ejecutar si la condición se cumple

# Ejemplo:
edad = 18

if edad >= 18:
	print("Eres mayor de edad")
"""
En este caso, si la variable edad es mayor o igual a 18, se ejecutará el bloque de código
dentro del if y se imprimirá el mensaje "Eres mayor de edad"
"""

# if else
"""
La estructura if else nos permite especificar un bloque de código alternativo 
que se ejecutará si la condicion del if es falsa.
La sintaxis es la siguiente:
"""
edad = 15

if edad >= 18:
	print("Eres mayor de edad")
else:
	print("Eres menor de edad")
"""
En este ejemplo si la variable edad es mayor o igual a 18, se ejecutará el bloque de código dentro del if
y se imprimira el mensaje "Eres mayor de edad". De lo contrario, se ejecutará el bloque de código dentro del else
y éste mostrará "Eres menor de edad"
"""

# if elif else
"""
La estructura if elif else nos permite especificar múltiples condiciones y bloques de código alternativos.
La sintaxis es la siguiente:
"""
calificacion = 85

if calificacion >= 90:
	print("Excelente")
elif calificacion >= 80:
	print("Muy bueno")
elif calificacion >= 70:
	print("Bueno")
else:
	print("Necesita mejorar")

# Ejemplo implementando un menú

menu_cli = """
			_____________________________________________
			|																						|
			|					MENU EN LINEA DE COMANDOS				 	|
			|___________________________________________|
			|																						|
			|			Seleccione una opción:								|
			|																						|
			|		1. Opcion 1															|
			|		2. Opcion 2															|
			|		3. Opcion 3															|
			|		4. Salir del menú												|
			|___________________________________________|
"""
print(menu_cli)
opcion = int(input("Indique una opción numérica: "))

if opcion = 1:
	print("Ha seleccionado la opcion 1")
	elif opcion = 2:
		print("Ha seleccionado la opcion 2")
	elif opcion = 3:
		print("Ha seleccionado la opcion 3")
	elif opcion = 4:
		print("Ha seleccionado la opcion 4. Hasta luego!!!")
else:
	print("La opcion seleccionada no es válida. Porfavor indique una opción del 1 al 4")

"""
Tal como se ve en éste ejemplo, se evalúan múltiples condiciones en orden.
Si la variable opcion es igual a 1, se imprime "Ha seleccionado la opcion 1".
Si no se cumple la primera condicion pero opcion es igual a 2, se muestra "Ha seleccionado la opcion 2".
Seguirá así hasta que una de las condiciones sea cumplida, si ninguna condición se cumple
se ejecutará el bloque del else mostrando el mensaje "La opcion seleccionada no es válida..."










