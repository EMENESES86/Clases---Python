# ***********************************************************************
# Introducción Avanzada a Python para Inteligencia Artificial
# Ejemplos prácticos para temas avanzados
# ***********************************************************************

# **************************************************************************
# 1. Comprensión de Listas

# Ejemplo 1: Crear una lista de los cubos de los números impares entre 1 y 10
cubos_impares = [i ** 3 for i in range(1, 11) if i % 2 != 0]
print(cubos_impares)  # Muestra: [1, 27, 125, 343, 729]

# Ejemplo 2: Generar una lista de pares de tuplas (n, n^2) para números de 1 a 5
pares_cuadrados = [(i, i ** 2) for i in range(1, 6)]
print(pares_cuadrados)  # Muestra: [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

# **************************************************************************
# 2. Manejo de Excepciones

# Ejemplo: Capturar múltiples excepciones
try:
    num = int(input("Ingresa un número: "))
    resultado = 10 / num
except ValueError:
    print("Error: Debes ingresar un número válido.")
except ZeroDivisionError:
    print("Error: No puedes dividir entre cero.")
finally:
    print("Fin del manejo de excepciones.")

# **************************************************************************
# 3. Clases y Objetos

# Ejemplo 1: Clases con métodos estáticos y de clase
class Circulo:
    pi = 3.1416

    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return Circulo.pi * (self.radio ** 2)

    @classmethod
    def desde_diametro(cls, diametro):
        return cls(diametro / 2)

    @staticmethod
    def es_radio_valido(radio):
        return radio > 0

# Crear un círculo desde el diámetro
circulo = Circulo.desde_diametro(10)
print(circulo.area())  # Muestra: 78.54

# Validar si el radio es válido
print(Circulo.es_radio_valido(5))  # Muestra: True
print(Circulo.es_radio_valido(-1))  # Muestra: False

# **************************************************************************
# 4. Funciones Lambda

# Ejemplo 1: Usar lambda para ordenar una lista de tuplas por el segundo valor
tuplas = [(1, 'b'), (3, 'a'), (2, 'c')]
tuplas_ordenadas = sorted(tuplas, key=lambda x: x[1])
print(tuplas_ordenadas)  # Muestra: [(3, 'a'), (1, 'b'), (2, 'c')]

# Ejemplo 2: Crear una función lambda para elevar un número a una potencia específica
potencia = lambda base, exponente: base ** exponente
print(potencia(2, 3))  # Muestra: 8

# **************************************************************************
# 5. Módulos y Paquetes

# Ejemplo: Calcular el área de un círculo usando `math.pi` en lugar de un valor aproximado
import math
radio = 5
area_circulo = math.pi * radio ** 2
print(f"El área del círculo es: {area_circulo}")  # Muestra: El área del círculo es: 78.53981633974483

# **************************************************************************
# 6. Numpy y Manipulación de Matrices

# Importar la librería NumPy
import numpy as np

# Ejemplo 1: Crear un array 3x3 y multiplicarlo por un escalar
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
resultado = arr * 2
print(resultado)
# Muestra:
# [[ 2  4  6]
#  [ 8 10 12]
#  [14 16 18]]

# Ejemplo 2: Sumar dos matrices 2x2
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
suma = A + B
print(suma)
# Muestra:
# [[ 6  8]
#  [10 12]]

# **************************************************************************
# 7. Decoradores

# Ejemplo: Crear un decorador que verifique si un número es positivo antes de ejecutar la función
def verificar_positivo(func):
    def envoltura(num):
        if num < 0:
            print("Error: El número debe ser positivo.")
        else:
            return func(num)
    return envoltura

@verificar_positivo
def imprimir_raiz_cuadrada(num):
    print(f"La raíz cuadrada de {num} es {math.sqrt(num)}")

imprimir_raiz_cuadrada(9)  # Muestra: La raíz cuadrada de 9 es 3.0
imprimir_raiz_cuadrada(-4)  # Muestra: Error: El número debe ser positivo.

# **************************************************************************
# 8. Context Managers

# Ejemplo: Leer un archivo con un context manager y manejar posibles excepciones
try:
    with open('archivo.txt', 'r') as archivo:
        contenido = archivo.read()
        print(contenido)
except FileNotFoundError:
    print("Error: El archivo no existe.")
# Si existe, mostrará el contenido del archivo; de lo contrario, mostrará el error.

# **************************************************************************
# 9. Generadores

# Ejemplo: Crear un generador que devuelva los primeros n números Fibonacci
def generador_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for numero in generador_fibonacci(7):
    print(numero)  # Muestra: 0, 1, 1, 2, 3, 5, 8

# **************************************************************************
# Conclusión

# Estos ejemplos avanzados refuerzan los conceptos más complejos de Python, como 
# la comprensión de listas, manejo de excepciones, programación orientada a objetos,
# funciones lambda, módulos, NumPy, decoradores, context managers, y generadores.
# Estos temas son fundamentales para el desarrollo de proyectos de IA.
