import numpy as np
import pandas as pd

archivo = 'Auto_Sales_data.csv'
data = pd.read_csv(archivo)  # Utiliza pd.read_csv() para cargar los datos desde un archivo CSV


#Muestren las primeras y últimas filas del dataset.
primeras = data.head()
ultimas = data.tail()

# Imprime las primeras y las últimas filas
print(f"Primeras filas:\n{primeras}")
print(f"Últimas 5 filas:\n{ultimas}")

# Muestra info del csv
data.info()

#Obtengan información general del dataset, como el número de filas y columnas, y los tipos de datos.
nfilas, ncolumnas = data.shape  #la funcion.shape devuelve una tupla que representa las dimensiones de la estructura de datos
print(f"Número de filas: {nfilas}")
print(f"Número de columnas: {ncolumnas}")

tipos = data.dtypes  #un atributo de un DataFrame que devuelve una Serie que contiene los tipos de datos de cada columna en el DataFrame
print(f"Tipos de datos de cada columna:{tipos}")  

