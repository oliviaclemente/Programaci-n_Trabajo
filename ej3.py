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

#que valores toma PRODUCTLINE
print(data['PRODUCTLINE'].unique())

#diagrama de cajas de PRICEEACH para Classic Cars
sns.boxplot(x='PRICEEACH', y='PRODUCTLINE', data=data[data['PRODUCTLINE']=='Classic Cars'], orient='h')
plt.title('Diagrama de cajas de PRICEEACH para Classic Cars')
plt.xlabel('PRICEEACH')
plt.ylabel('PRODUCTLINE')
plt.show()

#Histograma que muestra la distribución de cada Productline
sns.histplot(data=data, x='PRODUCTLINE', hue='PRODUCTLINE', multiple='stack')
plt.show()

#Identifiquen y analicen las correlaciones entre variables
#calcular el coeficiente de relación de Pearson para ver la correlación lineal
corr = data.corr(method='pearson')

# Blucle for que sustituye los números por palabras
for i in corr.columns:
    for j in corr.columns:
        if corr[i][j] == 1:
            corr[i][j] = 'PERFECTA (+)'
        elif corr[i][j] == -1:
            corr[i][j] = 'PERFECTA (-)'
        elif corr[i][j] < 1 and corr[i][j] >= 0.5:
            corr[i][j] = 'FUERTE (+)'
        elif corr[i][j] > -1 and corr[i][j] <= -0.5:
            corr[i][j] = 'FUERTE (-)'
        elif corr[i][j] < 0.5 and corr[i][j] >= 0.3:
            corr[i][j] = 'MODERADA (+)'
        elif corr[i][j] > -0.5 and corr[i][j] <= -0.3:
            corr[i][j] = 'MODERADA (-)'
        elif corr[i][j] < 0.3 and corr[i][j] >= 0.1:
            corr[i][j] = 'DEBIL (+)'
        elif corr[i][j] > -0.3 and corr[i][j] <= -0.1:
            corr[i][j] = 'DEBIL (-)'
        else:
            corr[i][j] = 'NULA'

print(corr)

#Calcular la recta de regresión
import numpy as np
import matplotlib.pyplot as plt

# Datos de PRICEEACH Y SALES
PRICEEACH = data['PRICEEACH'].values
SALES = data['SALES'].values

# Calcular la recta de regresión
pendiente, ordenada_al_origen = np.polyfit(PRICEEACH, SALES, 1)
#np.polyfit se utiliza para calcular directamente la pendiente y la ordenada al origen de la recta de regresión

# Imprimir los coeficientes
print(f"Pendiente: {pendiente}")
print(f"Ordenada_al_origen: {ordenada_al_origen}")

# Visualizar los datos y la recta de regresión
plt.scatter(PRICEEACH, SALES, label='Datos reales')
plt.plot(PRICEEACH, pendiente * PRICEEACH + ordenada_al_origen, color='red', label='Recta de regresión')
plt.xlabel('PRICEEACH')
plt.ylabel('SALES')
plt.legend()
plt.show()
