# Bucles - loops
"""
Los bucles nos permiten repetir un bloque de código varias veces. En python, los bucles más comunes son 'for' y 'while'.
"""

# For
"""
El bucle 'for' se utiliza para iterar sobre una secuencia (como una lista, tupla o una cadena) o cualquier objeto iterable.
La sintaxis es la siguiente:
"""
'''
for (variable) in "secuencia":
    bloque de codigo a repetir
    instrucciones
'''
# Ejemplo:
variable = 0
print("Ejemplo de 'for':")
for variable in range(0, 11):
    print(variable)
    """ 
    Ésto creará un contador repitiendo el print desde el 0 hasta el 10. Por qué 11 si solo muestra hasta el 10?
    Respuesta: Cuando usas range() en Python, piénsalo como una forma de contar. El primer número que pones es el punto de inicio, y el segundo número es el punto donde te detienes, pero no lo incluyes.

    Por ejemplo, si dices que quieres contar desde 0 hasta 11, en realidad solo contarás hasta el 10. El 11 no se incluye.

    Si quieres contar hasta el 11, debes decirle que se detenga en 12. Así que siempre recuerda: el primer número se cuenta, pero el segundo no. Es como si el segundo número estuviera "fuera de la fiesta".

    La razón detrás de esto se basa en la forma en que los programadores piensan sobre los rangos y la consistencia en el manejo de índices.

        * Contar desde cero: En programación, empezamos a contar desde cero en lugar de uno. Esto se debe a que muchas herramientas, como listas, utilizan este sistema. Así, el primer número que eliges se incluye porque es donde comienza la cuenta.

        * Facilidad de uso: Hacer que el segundo número no se cuente hace que sea más fácil trabajar con rangos. Por ejemplo, si tienes una lista de 10 cosas, puedes usar range(0, 10), y esto coincide con los lugares de esas cosas, que van de 0 a 9. Así, no hay confusión.

        * Cálculos simples: También hay una razón matemática. Cuando defines un rango, puedes calcular cuántos números hay simplemente restando el primer número del segundo. Por ejemplo, en range(0, 10), hay 10 números porque 10 menos 0 es 10.

    Este enfoque ayuda a que todo sea más claro y consistente cuando programamos.
    """

    # Veamos un ejemplo de contador que no comience por 0
print("_________________") # Esto es solo para separar del ejemplo anterior
contador = 0

for contador in range(1, 11):
    print(contador)
    # Tal como se ve en el resultado, aunque comencemos por el 1, siempre tendremos que especificar el 11 para que termine en 10

    # Veamos otro ejemplo de contador que termine por 10
print("_________________") # Esto es solo para separar del ejemplo anterior
contador2 = 0

for contador2 in range(1, 10):
    print(contador2)
    # Vemos que ahora el resultado muestra 9 en lugar de 10.
    """
    Esto comunmente se conoce como índice y es importante que el segundo índice siempre termine un número mayor al número que queremos representar.
    """

    # Veamos un ejemplo de contador pero usando strings
print("_________________") # Esto es solo para separar del ejemplo anterior
letras = ["a", "b", "c", "d", "e", "f", "g"]

for i in range(len(letras)):
    print(letras[i])
    # Tal como se ve en el resultado, para seguir usando range(), se debe pensar en una lista y tendrías que referenciar la lista de letras mediante su índice.
    """
    En este caso, len(letras) te da la cantidad de letras en la lista, y letras[i] accede a cada letra usando su índice. Esto mantiene el concepto de "rango" al mismo tiempo que muestras las letras.

    * Listas de letras: Cuando quieres mostrar letras en lugar de números, puedes usar una lista. Una lista es como una caja donde guardas cosas, en este caso, letras. Así, en vez de usar un rango de números, simplemente recorres cada letra de la lista.

    * Recorrer la lista: Cuando usas un bucle for, puedes ir letra por letra de la lista sin preocuparte por los números. Cada vez que el bucle pasa, saca una letra de la lista y la muestra.

    * Usar índices: Si prefieres usar range(), puedes hacerlo accediendo a las letras por su posición en la lista. La función len() te dice cuántas letras hay, y luego puedes usar un número para "apuntar" a cada letra en esa posición.
    """
# Veremos mas casos de lista más adelante.

# While
"""
El bucle while se utiliza para repetir un bloque de código mientras una condición sea verdadera.
La sintaxis es la siguiente:
"""
'''
while variable:
    bloque de código a repetir
    instrucciones
'''
# Ejemplo (También se pueden usar contadores):
print("_________________") # Esto es solo para separar del ejemplo anterior
print("Ejemplo de 'while':")
contador3 = 0
while contador3 < 5:
    print(contador3)
    contador3 += 1

"""
En este ejemplo, el bucle while se ejecuta mientras la variable contador sea menor que 5. En cada iteración, se imprime el valor de contador y luego se incrementa en 1 mediante la instrucción contador +=1
El bucle se detendrá cuando el contador alcance el valor de 5.

IMPORTANTE: Tener cuidado al usar el bucle 'while', ya que, si la condición nunca se vuelve falsa, el bucle se ejecutará indefinidamente, lo que se conoce como un bucle infinito y causará problemas de rendimiento en tiempo de ejecución sobrecalentando el CPU.
"""

# Control de bucles
"""
Python proporciona algunas instrucciones especiales para controlar el flujo de ejecución dentro de los bucles.
"""
# Uso de break
"""
La instrucción break se utiliza para salir prematuramente de un bucle, independientemente de la condición. Cuando se encuentra un break, el bucle se detiene y el flujo de ejecución continúa con la siguiente instrucción fuera del bucle.
"""

# Ejemplo:
print("_________________") # Esto es solo para separar del ejemplo anterior
numero = 0
print("Ejemplo de 'break':")
while True:
    print(numero)
    numero += 1

    if numero == 5:
        break
"""
En éste ejemplo, el bucle 'while' se ejecuta indefinidamente debido a la condición True. Sin embargo, dentro del bucle se utiliza una estructura condicional 'if' para verificar si contador es igual a 5. Cuando se cumple ésta condición, se ejecuta la instrucción break, lo que hace que el bucle se detenga y el flujo de ejecución continúe con la siguiente instrucción fuera del bucle.
"""

# Uso de continue
"""
La instrucción 'continue' se utiliza para resaltar el resto del bloque de código dentro de un bucle y pasar a la siguiente iteración.
"""
# Ejemplo:
print("_________________") # Esto es solo para separar del ejemplo anterior
print("Ejemplo de 'continue':")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
"""
En éste ejemplo, el bucle 'for' itera sobre los números del 0 al 9 utilizando la función 'range()'. Dentro del bucle, se verifica si el número es divisible por 2 utilizando el operador de módulo %. Si el número es divisible por 2 (es decir, si es par), se ejecuta la instrucción 'continue', lo que hace que se salte el resto del bloque de código y se pase a la siguiente iteración del bucle. Como resultado, solo se imprimirán los números impares.
"""

# Uso de pass
"""
La instrucción 'pass' es una operación nula que no hace nada. Se utiliza como marcador de posición cuando se requiere una instrucción sintácticamente, pero no se desea realizar ninguna acción.
"""
# Ejemplo:
print("_________________") # Esto es solo para separar del ejemplo anterior
print("Ejemplo de 'pass':")

for i in range(5):
    pass
"""
En éste ejemplo, el bucle 'for' itera sobre los números del 0 al 4, pero no se realiza ninguna acción dentro del bucle debido a la instrucción 'pass'. Ésto puede ser útil cuando se está desarrollando un programa y se desea reservar un bloque de código para implementarlo más adelante.
"""

# Resúmen de éste capítulo:
"""
La estructuras de control son herramientas poderosas que nos permiten controlar el flujo de ejecución de nuestros programas. Con las estructuras condicionales 'if, if-else, if-elif-else' podemos tomar decisiones basadas en condiciones, mientras que con los bucles 'for, while' podemos repetir bloques de código varias veces. Además, las instrucciones 'break, continue y pass' nos brindan un control adicional sobre el comportamiento de los bucles.
"""