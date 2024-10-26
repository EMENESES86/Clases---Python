# ***********************************************************************
# Introducción a la Importación de Librerías en Python
# Python tiene muchas librerías que permiten realizar tareas complejas con
# pocas líneas de código. A continuación, se explican cómo importar librerías, 
# su instalación, y ejemplos prácticos.
# ***********************************************************************

# **************************************************************************
# Cómo importar librerías

# Ejemplo 1: Importar toda la librería
import math
print(math.sqrt(16))  # Usa la función sqrt de la librería math

# Otro ejemplo:
print(math.factorial(5))  # Calcula el factorial de 5

# Ejemplo 2: Importar una función específica
from math import sqrt
print(sqrt(25))  # Directamente usa sqrt sin el prefijo 'math.'

# Otro ejemplo:
from math import pi
print(pi)  # Imprime el valor de pi

# Ejemplo 3: Usar un alias para una librería
import numpy as np
arr = np.array([1, 2, 3])
print(arr)  # Crea un array usando NumPy

# Otro ejemplo:
arr = np.zeros((3, 3))  # Crea una matriz de ceros de 3x3
print(arr)

# **************************************************************************
# Librerías más usadas en Python
# A continuación, algunas de las librerías más utilizadas en desarrollo general.

# 1. NumPy: Manipulación de arrays y operaciones matemáticas avanzadas
# Instalar: pip install numpy
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)  # Imprime un array de NumPy

# Otro ejemplo:
matriz = np.array([[1, 2], [3, 4]])
print(np.transpose(matriz))  # Transpone la matriz

# Crear un array de 3x3 lleno de unos
unos = np.ones((3, 3))
print(unos)

# Crear una matriz identidad de 4x4
identidad = np.eye(4)
print(identidad)

# 2. Pandas: Manejo y análisis de datos tabulares
# Instalar: pip install pandas
import pandas as pd
df = pd.DataFrame({'Columna1': [1, 2], 'Columna2': [3, 4]})
print(df)  # Crea un DataFrame básico

# Otro ejemplo:
df2 = pd.read_csv('/archivo.csv')  # Lee un archivo CSV
print(df2.head())  # Muestra las primeras filas del DataFrame

# Crear un DataFrame de una lista de diccionarios
datos = [{'nombre': 'Ana', 'edad': 23}, {'nombre': 'Luis', 'edad': 30}]
df = pd.DataFrame(datos)
print(df)

# Filtrar filas donde la edad es mayor que 25
df_filtrado = df[df['edad'] > 25]
print(df_filtrado)

# 3. Matplotlib: Visualización de datos con gráficos
# Instalar: pip install matplotlib
import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.show()  # Crea y muestra un gráfico de línea

# Otro ejemplo:
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
plt.bar(x, y)  # Crea un gráfico de barras
plt.show()

# Crear un histograma de datos aleatorios
data = np.random.randn(1000)
plt.hist(data, bins=30)
plt.show()

# Crear un gráfico de dispersión
x = np.random.rand(50)
y = np.random.rand(50)
plt.scatter(x, y)
plt.show()

# 4. Requests: Realizar solicitudes HTTP
# Instalar: pip install requests
import requests
response = requests.get('https://api.github.com')
print(response.status_code)  # Imprime el estado de la respuesta

# Otro ejemplo:
response = requests.get('https://api.github.com/users/octocat')
print(response.json())  # Devuelve el contenido en formato JSON

# Enviar datos con una petición POST
data = {'key': 'value'}
response = requests.post('https://httpbin.org/post', data=data)
print(response.json())

# Descargar una imagen de internet
url = 'https://via.placeholder.com/150'
img_data = requests.get(url).content
with open('imagen.jpg', 'wb') as handler:
    handler.write(img_data)

# **************************************************************************
# Librerías Esenciales para Inteligencia Artificial
# A continuación, algunas librerías populares para IA y machine learning.

# 1. TensorFlow: Librería para crear y entrenar modelos de aprendizaje profundo
# Instalar: pip install tensorflow
import tensorflow as tf
print(tf.__version__)  # Verifica la versión de TensorFlow

# Otro ejemplo:
a = tf.constant(5)
b = tf.constant(3)
print(tf.add(a, b))  # Suma dos tensores

# Crear un tensor de ceros
tensor = tf.zeros([3, 3])
print(tensor)

# Definir una red neuronal simple usando Keras (interfaz de TensorFlow)
from tensorflow.keras import layers
model = tf.keras.Sequential([layers.Dense(64, activation='relu')])
print(model.summary())

# 2. Keras: API de alto nivel para redes neuronales
# Instalar: pip install keras (aunque ya está incluida en TensorFlow)
from tensorflow import keras
model = keras.models.Sequential()
model.add(keras.layers.Dense(64, activation='relu', input_shape=(32,)))
model.add(keras.layers.Dense(1))
model.compile(optimizer='adam', loss='mean_squared_error')

# Otro ejemplo:
# Crear y compilar un modelo secuencial con múltiples capas
model2 = keras.Sequential([
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])
model2.compile(optimizer='adam', loss='sparse_categorical_crossentropy')
print(model2.summary())

# 3. PyTorch: Framework para redes neuronales dinámicas
# Instalar: pip install torch
import torch
x = torch.tensor([1.0, 2.0, 3.0])
print(x)  # Imprime un tensor de PyTorch

# Otro ejemplo:
y = torch.ones(3)
z = x + y  # Suma de tensores
print(z)

# Crear un tensor de números aleatorios
tensor_random = torch.randn(3, 3)
print(tensor_random)

# Crear una red neuronal simple en PyTorch
import torch.nn as nn
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(10, 5)
    
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        return x

net = Net()
print(net)

# 4. Scikit-learn: Algoritmos de machine learning
# Instalar: pip install scikit-learn
from sklearn import datasets
iris = datasets.load_iris()
print(iris.data)  # Carga el conjunto de datos Iris

# Otro ejemplo:
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit([[0, 0], [1, 1], [2, 2]], [0, 1, 2])  # Entrenar un modelo de regresión
print(model.coef_)  # Muestra los coeficientes del modelo

# Usar un clasificador K-Nearest Neighbors
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(iris.data, iris.target)
print(knn.predict([[5.1, 3.5, 1.4, 0.2]]))  # Clasificar un nuevo dato
