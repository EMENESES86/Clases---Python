# ***********************************************************************
# Introducción a Python para los temas de Inteligencia Artificial
# Aquí exploraremos conceptos básicos de Python, útiles para AI.
# ***********************************************************************

# **************************************************************************
# 1. Variables y Tipos de Datos

# Ejemplo 1: Operaciones con variables
# Declara dos variables numéricas y realiza operaciones básicas con ellas.
num1 = 15
num2 = 8
resultado_suma = num1 + num2
resultado_producto = num1 * num2
print(f"Suma: {resultado_suma}, Producto: {resultado_producto}")
# Salida esperada: Suma: 23, Producto: 120

# Ejemplo 2: Uso de diferentes tipos de datos
# Usa variables de tipo cadena, flotante y booleano para describir a una persona.
nombre = "Carlos"
edad = 25
es_estudiante = True
print(f"Nombre: {nombre}, Edad: {edad}, Estudiante: {es_estudiante}")
# Salida esperada: Nombre: Carlos, Edad: 25, Estudiante: True

# **************************************************************************
# 2. Condicionales: if, elif, else

# Ejemplo 1: Determinar si un número es positivo, negativo o cero
numero = -7
if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")
# Salida esperada: El número es negativo.

# Ejemplo 2: Categorizar una persona según su edad
edad = 16
if edad >= 18:
    print("Eres mayor de edad.")
elif 13 <= edad < 18:
    print("Eres un adolescente.")
else:
    print("Eres menor de edad.")
# Salida esperada: Eres un adolescente.

# **************************************************************************
# 3. Bucles: for y while

# Ejemplo 1: Encontrar los números pares entre 1 y 10 usando un bucle for
for i in range(1, 11):
    if i % 2 == 0:
        print(f"{i} es par.")
# Salida esperada: 2 es par, 4 es par, 6 es par, 8 es par, 10 es par.

# Ejemplo 2: Contar los intentos hasta que el usuario escriba "salir"
intentos = 0
entrada = ""
while entrada != "salir":
    entrada = input("Escribe algo (escribe 'salir' para detener): ")
    intentos += 1
print(f"Intentos: {intentos}")
# Salida esperada: Dependerá de cuántas veces el usuario ingrese texto antes de escribir 'salir'.

# **************************************************************************
# 4. Funciones

# Ejemplo 1: Calcular el factorial de un número usando una función
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Muestra: 120

# Ejemplo 2: Función para verificar si un número es primo
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(es_primo(7))  # Muestra: True
print(es_primo(10))  # Muestra: False

# **************************************************************************
# 5. Variables Globales y Locales

# Ejemplo: Contador global y local
contador_global = 0  # Variable global

def incrementar_contador_local():
    contador_local = 0  # Variable local
    contador_local += 1
    print(f"Contador local: {contador_local}")

def incrementar_contador_global():
    global contador_global
    contador_global += 1
    print(f"Contador global: {contador_global}")

incrementar_contador_local()  # Muestra: Contador local: 1
incrementar_contador_global()  # Muestra: Contador global: 1
incrementar_contador_global()  # Muestra: Contador global: 2

# **************************************************************************
# 6. Predicados

# Ejemplo 1: Predicado que verifica si una palabra contiene una letra específica
def contiene_letra(palabra, letra):
    return letra in palabra

print(contiene_letra("Python", "y"))  # Muestra: True
print(contiene_letra("Python", "z"))  # Muestra: False

# Ejemplo 2: Predicado que verifica si una lista está vacía
def lista_vacia(lista):
    return len(lista) == 0

print(lista_vacia([1, 2, 3]))  # Muestra: False
print(lista_vacia([]))  # Muestra: True

# **************************************************************************
# 7. Comentarios en Python

# Ejemplo práctico con comentarios
# Definimos una función que calcula el área de un círculo
def area_circulo(radio):
    # La fórmula es área = pi * radio^2
    pi = 3.1416
    return pi * radio ** 2

# Llamamos a la función con radio 5
print(area_circulo(5))  # Muestra: 78.54

# **************************************************************************
# 8. Listas y Operaciones Básicas

# Ejemplo 1: Ordenar una lista de números
numeros = [5, 3, 8, 2, 1]
numeros.sort()
print(f"Lista ordenada: {numeros}")  # Muestra: Lista ordenada: [1, 2, 3, 5, 8]

# Ejemplo 2: Multiplicar cada número de una lista por 2
lista = [1, 2, 3, 4, 5]
dobles = [x * 2 for x in lista]
print(dobles)  # Muestra: [2, 4, 6, 8, 10]

# **************************************************************************
# Conclusión
# Con estos ejemplos, puedes entender y practicar algunos de los conceptos básicos
# de Python. Estos conocimientos son fundamentales para adentrarse en los
# proyectos de Inteligencia Artificial.
