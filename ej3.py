'''Análisis exploratorio de datos (EDA):
• Calculen estadísticas básicas de las columnas numéricas media, 
mediana, desviación estándar usando funciones personalizadas que 
tendréis que crear vosotros.
• Crear gráficos para visualizar la distribución de los datos, como 
histogramas y diagramas de caja.
• Identifiquen y analicen las correlaciones entre variables.
'''
import numpy as np
import pandas as pd

archivo = 'Auto_Sales_data.csv'
data = pd.read_csv(archivo)  # Utiliza pd.read_csv() para cargar los datos desde un archivo CSV

primeras = data.head()
ultimas = data.tail()

# Imprime las primeras y las últimas filas
print(f"Primeras filas:\n{primeras}")
print(f"Últimas 5 filas:\n{ultimas}")

# Muestra info del csv
data.info()

nfilas, ncolumnas = data.shape
print(f"Número de filas: {nfilas}")
print(f"Número de columnas: {ncolumnas}")

tipos = data.dtypes
print(f"Tipos de datos de cada columna:{tipos}")

# Calcular media, mediana, desviación estándar de la columna 'QUANTITYORDERED'
media = data['QUANTITYORDERED'].mean()
print(media)

mediana = data['QUANTITYORDERED'].median()
print(mediana)

desviacion = data['QUANTITYORDERED'].std()
print(desviacion)

# Calcular media, mediana, desviación estándar de la columna 'PRICEEACH'
media = data['PRICEEACH'].mean()
print(media)

mediana = data['PRICEEACH'].median()
print(mediana)

desviacion = data['PRICEEACH'].std()
print(desviacion)

# Calcular media, mediana, desviación estándar de la columna 'SALES'
media = data['SALES'].mean()
print(media)

mediana = data['SALES'].median()
print(mediana)

desviacion = data['SALES'].std()
print(desviacion)

# Calcular media, mediana, desviación estándar de la columna 'MSRP'
media = data['MSRP'].mean()
print(media)

mediana = data['MSRP'].median()
print(mediana)

desviacion = data['MSRP'].std()
print(desviacion)

#Crear gráficos para visualizar la distribución de los datos, como histogramas y diagramas de caja.
import matplotlib.pyplot as plt
import seaborn as sns

# Histograma de la columna 'PRICEEACH'
plt.hist(data['PRICEEACH'])
plt.xlabel('Precio')
plt.ylabel('Frecuencia')
plt.title('Histograma de la columna PRICEEACH')
plt.show()