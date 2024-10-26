# ***********************************************************************
# Introducción Avanzada a Python para Inteligencia Artificial

# En esta introducción avanzada, profundizaremos en conceptos y herramientas 
# de Python que son esenciales para el desarrollo de proyectos más complejos 
# en Inteligencia Artificial. Estos incluyen estructuras de datos más avanzadas,
# comprensión de listas, manejo de excepciones, clases y objetos, entre otros.
# ***********************************************************************

# **************************************************************************
# 1. Comprensión de Listas

# La comprensión de listas permite construir listas de manera concisa, utilizando
# un formato más compacto que los bucles tradicionales.

cuadrados = [i ** 2 for i in range(1, 11)]
print(cuadrados)  # Muestra: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Incluso podemos incluir condiciones en la comprensión de listas
pares = [i for i in range(1, 11) if i % 2 == 0]
print(pares)  # Muestra: [2, 4, 6, 8, 10]

# **************************************************************************
# 2. Manejo de Excepciones

# El manejo de excepciones es crucial cuando trabajamos con datos del mundo real.
# Python usa el bloque try-except para manejar excepciones.

try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: No puedes dividir entre cero.")
finally:
    print("Este bloque se ejecuta siempre, haya o no error.")

# **************************************************************************
# 3. Clases y Objetos

# La programación orientada a objetos es un paradigma clave para estructurar 
# código en proyectos grandes, como los relacionados con la IA.

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, me llamo {self.nombre} y tengo {self.edad} años."

persona1 = Persona("Carlos", 30)
print(persona1.saludar())  # Muestra: Hola, me llamo Carlos y tengo 30 años.

# Herencia
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

    def estudiar(self):
        return f"{self.nombre} está estudiando {self.carrera}."

estudiante = Estudiante("Ana", 22, "Ingeniería")
print(estudiante.estudiar())  # Muestra: Ana está estudiando Ingeniería.

# **************************************************************************
# 4. Funciones Lambda

# Las funciones lambda son funciones anónimas y se utilizan para tareas simples
# que requieren una función de una sola línea.

sumar = lambda a, b: a + b
print(sumar(5, 3))  # Muestra: 8

# Filtrar una lista con función lambda
numeros = [1, 2, 3, 4, 5, 6]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Muestra: [2, 4, 6]

# **************************************************************************
# 5. Módulos y Paquetes

# Los módulos permiten organizar el código en archivos separados. Python tiene 
# una extensa librería estándar que contiene muchos módulos útiles para la IA.

import math
print(math.sqrt(16))  # Muestra: 4.0

from math import factorial
print(factorial(5))  # Muestra: 120

# **************************************************************************
# 6. Numpy y Manipulación de Matrices

# En proyectos de Inteligencia Artificial, las matrices son estructuras de datos 
# fundamentales. NumPy es una librería que proporciona herramientas eficientes 
# para trabajar con matrices.

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)  # Muestra: [1 2 3 4 5]

matriz = np.array([[1, 2], [3, 4]])
print(matriz)

suma = arr + 5
print(suma)  # Muestra: [6 7 8 9 10]

# **************************************************************************
# 7. Decoradores

# Los decoradores son funciones que modifican el comportamiento de otras funciones.
# Se usan mucho en Python para agregar funcionalidades de manera concisa.

def decorador(func):
    def envoltura():
        print("Esto se ejecuta antes de la función original.")
        func()
        print("Esto se ejecuta después de la función original.")
    return envoltura

@decorador
def funcion_principal():
    print("Esta es la función principal.")

funcion_principal()

# **************************************************************************
# 8. Context Managers

# Los context managers permiten manejar recursos como archivos de manera eficiente,
# liberando automáticamente el recurso cuando ya no es necesario.

with open('archivo.txt', 'w') as archivo:
    archivo.write("¡Hola desde Python!")

# **************************************************************************
# 9. Generadores

# Los generadores permiten crear funciones que devuelven un conjunto de valores 
# uno a la vez, en lugar de devolverlos todos al mismo tiempo.

def contador(max):
    i = 1
    while i <= max:
        yield i
        i += 1

for numero in contador(5):
    print(numero)  # Muestra: 1, 2, 3, 4, 5

# **************************************************************************
# Conclusión

# Esta introducción avanzada cubre temas más complejos que son esenciales 
# para trabajar con Python en proyectos de Inteligencia Artificial. 
# La comprensión de listas, manejo de excepciones, clases y objetos, 
# decoradores, y módulos como NumPy te ayudarán a resolver problemas 
# más sofisticados y optimizar el rendimiento de tus aplicaciones.
