#Operadores
"""
Los operadores son símbolos especiales que nos permiten realizar operaciones en variables y valores.
Python proporciona diferentes tipos de operadores para realizar operaciones aritméticas, comparaciones y operaciones lógicas
"""

# Aritméticos
"""
Los operadores aritméticos se utilizan para realizar opraciones matemáticas básicas.
Los principales operadores aritméticos en python son:
"""
# Suma (+): suma dos valores
# Resta (-): resta el segundo valor del primero
# Multiplicación (*): multiplica dos valores
# División (/): divide el primer valor por el segundo y devuelve un resultado de tipo flotante
# División entera (//): divide el primer valor por el segundo y devuelve un resultdo de tipo entero descartando la parte decimal
# Módulo (%): devuelve el resto de la división entre el primer valor y el segundo
# Exponenciación (**): eleva el primer valor a la potencia del segundo

#Ejemplos:

a = 10
b = 3
suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b
division_entera = a // b
modulo = a % b
exponenciacion = a ** b

print(suma)
print(resta)
print(multiplicacion)
print(division)
print(division_entera)
print(modulo)
print(exponenciacion)

# De comparación
"""
Los operadores de comparación se utilizan para comparar dos valores y devuelven un valor booleano
como True o False, según el resultado de la comparación. Los operadores de comparación en Python son:
"""
# Igual a (==): devuelve True si ambos valores son iguales, de lo contrario sera False
# Diferente de (!=): devuelve True si los valores son diferentes
# Mayor que (>): devuelve True si el primer valor es mayor que el segundo
# Menor que (<): devuelve True si el primer valor es menor que el segundo
# Mayor o igual que (>=): devuelve True si el primer valor es mayor o igual que el segundo
# Menor o igual que (<=): devuelve True si el primer valor es menor o igual que el segundo

# Ejemplos:

a = 10
b = 3

igual_a = a == b
diferente_de = a != b
mayor_que = a > b
menor_que = a < b
mayor_igual_que = a >= b
menor_igual_que = a <= b

# Lógicos
"""
Los operadores lógicos se utilizan para combinar expresiones condicionales y evaluar múltiples condiciones.
Los operadores lógicos en Python son:
"""
# and : devuelve True si ambas condiciones son verdaderas
# or : devuelve True si al menos una de las condiciones es verdadera
# not : invierte el valor de una condición, devuelve True si la condición es falsa y False si es verdadera

# Ejemplo:
a = 10
b = 3

result_and = (a > 5) and (b < 5)
result_or = (a > 5) or (b < 5)
result_not = not (a > 5)
# Estos operadores se pueden utilizar para realizar cálculos, tomar decisiones basadas en comparaciones
# y combinar condiciones lógicas en los programas.
