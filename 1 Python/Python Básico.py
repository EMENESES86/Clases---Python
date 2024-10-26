# Introducción a Python para los temas de Inteligencia Artificial

# En esta introducción, veremos algunos conceptos básicos de Python que son esenciales para comprender los ejemplos de Inteligencia Artificial que trabajaremos. 
# Python es un lenguaje de programación popular por ser fácil de aprender y muy utilizado en el campo de la Inteligencia Artificial. Vamos a comenzar con lo básico:

# **************************************************************************
# 1. Variables y Tipos de Datos
# Las variables nos permiten almacenar valores que luego podremos usar o modificar. En Python, no es necesario especificar el tipo de dato de una variable, ya que Python lo determina automáticamente.

# Declarando variables
numero = 10  # Esto es un número entero
texto = "Hola, mundo"  # Esto es una cadena de texto (string)
flotante = 3.14  # Esto es un número decimal (float)
booleano = True  # Esto es un valor booleano (True o False)

# Imprimir el valor de una variable
print(numero)  # Muestra: 10
print(texto)  # Muestra: Hola, mundo
print(flotante)  # Muestra: 3.14
print(booleano)  # Muestra: True

# **************************************************************************
# 2. Condicionales: if, elif, else
# Los condicionales permiten ejecutar diferentes códigos en función de una condición.

# Ejemplo de condicional
edad = 18
if edad >= 18:
    print("Eres mayor de edad.")  # Se ejecuta si la edad es 18 o mayor
elif edad >= 13:
    print("Eres un adolescente.")  # Se ejecuta si la edad está entre 13 y 17
else:
    print("Eres menor de edad.")  # Se ejecuta si la edad es menor a 13


# **************************************************************************
# 3. Bucles: for y while
# Los bucles nos permiten repetir acciones varias veces. Python tiene dos tipos principales de bucles: for y while.

# Bucle for que imprime los números del 1 al 5
for i in range(1, 6):
    print(i)  # Muestra: 1, 2, 3, 4, 5

# Bucle for que recorre una lista de nombres
nombres = ["Ana", "Luis", "Pedro"]
for nombre in nombres:
    print(nombre)  # Muestra: Ana, Luis, Pedro

# Bucle while que cuenta hacia atrás desde 5
contador = 5
while contador > 0:
    print(contador)  # Muestra: 5, 4, 3, 2, 1
    contador -= 1  # Resta 1 al contador en cada iteración

# Bucle while que se detiene cuando el usuario ingresa 'salir'
entrada = ""
while entrada != "salir":
    entrada = input("Escribe algo (escribe 'salir' para detener): ")
    print(f"Ingresaste: {entrada}")

# **************************************************************************
# 4. Funciones
# Una función es un bloque de código reutilizable que realiza una tarea específica.

# Definición de una función simple
# Esta función recibe un número y devuelve su cuadrado
def cuadrado(numero):
    return numero * numero

# Llamar a la función
resultado = cuadrado(4)
print(resultado)  # Muestra: 16

# Función que imprime un saludo personalizado
def saludar(nombre):
    print(f"Hola, {nombre}!")

saludar("Carlos")  # Muestra: Hola, Carlos!


# **************************************************************************
# 5. Variables Globales y Locales
# Variables locales: Se definen dentro de una función y solo pueden ser usadas dentro de ella.
# Variables globales: Se definen fuera de cualquier función y pueden ser usadas en cualquier parte del código.

x_global = 10  # Variable global

def mi_funcion():
    x_local = 5  # Variable local
    print(x_local)  # Muestra: 5

mi_funcion()
print(x_global)  # Muestra: 10

# Modificar una variable global dentro de una función
def modificar_global():
    global x_global
    x_global = 20  # Cambia el valor de la variable global

modificar_global()
print(x_global)  # Muestra: 20



# **************************************************************************
# 6. Predicados
# Un predicado es una función que devuelve True o False. Los predicados se usan para hacer decisiones o comprobaciones.

# Definir un predicado que verifica si un número es par
def es_par(numero):
    return numero % 2 == 0

# Usar el predicado
print(es_par(4))  # Muestra: True
print(es_par(5))  # Muestra: False

# Predicado que verifica si un texto contiene más de 5 caracteres
def es_largo(texto):
    return len(texto) > 5

print(es_largo("Hola"))  # Muestra: False
print(es_largo("Python"))  # Muestra: True


# **************************************************************************
# 7. Comentarios en Python
# Los comentarios se utilizan para explicar el código y hacer que sea más fácil de entender. En Python, los comentarios comienzan con el símbolo #.

# Esto es un comentario
# La siguiente línea imprime "Hola, mundo"
print("Hola, mundo")

# Comentarios multilínea (usando triple comillas)
"""
Este es un comentario de varias líneas.
Puede ser útil para explicar partes complejas del código.
"""
print("Fin del ejemplo de comentarios")



# **************************************************************************
# 8. Listas y Operaciones Básicas
# Las listas son colecciones que permiten almacenar múltiples valores.

# Crear una lista de números
numeros = [1, 2, 3, 4, 5]

# Acceder a elementos de la lista
print(numeros[0])  # Muestra: 1 (primer elemento)
print(numeros[-1])  # Muestra: 5 (último elemento)

# Agregar un elemento a la lista
numeros.append(6)
print(numeros)  # Muestra: [1, 2, 3, 4, 5, 6]

# Eliminar un elemento de la lista
numeros.remove(3)
print(numeros)  # Muestra: [1, 2, 4, 5, 6]

# Iterar sobre una lista
for num in numeros:
    print(num)


# **************************************************************************
# Conclusión
# Estos conceptos básicos de Python te ayudarán a comprender los ejemplos de Inteligencia Artificial que veremos. Si tienes alguna duda sobre cómo funcionan, no dudes en preguntar.
# Hemos cubierto variables, condicionales, bucles, funciones, variables globales y locales, predicados, comentarios y listas, que son fundamentales para empezar a trabajar con Python en el contexto de la Inteligencia Artificial.

