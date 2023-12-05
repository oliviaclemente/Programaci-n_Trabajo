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


#Mirar que columnas tienen datos numéricos
#print(df.select_dtypes(include=[np.number]).columns)
#Haz los calculos solo para las columnas donde es útil y tiene sentido

#crea una función para calcular la media
def media(columna):
    suma = 0
    for i in columna:
        suma += i
    return suma / len(columna)

#crea una función para calcular la mediana
def mediana(columna):
    columna_ordenada = sorted(columna)
    if len(columna) % 2 == 0:
        mediana = (columna_ordenada[int(len(columna) / 2)] + columna_ordenada[int(len(columna) / 2) - 1]) / 2
    else:
        mediana = columna_ordenada[int(len(columna) / 2)]
    return mediana

#crea una función para calcular la desviación estándar
def desviacion_estandar(columna):
    suma = 0
    for i in columna:
        suma += (i - media(columna))**2
    return (suma / len(columna))**0.5

#calcular la media, mediana y desviación estandar de la columna cantidad_de_pedidos
#print(f"Media de cantidad de pedidos: {media(df['cantidad_de_pedidos'])}")
#print(f"Mediana de cantidad de pedidos: {mediana(df['cantidad_de_pedidos'])}")
#print(f"Desviación estándar de cantidad de pedidos: {desviacion_estandar(df['cantidad_de_pedidos'])}")

#calcular la media, mediana y desviación estandar de la columna precio_cada_pedido
#print(f"Media de precio cada pedido: {media(df['precio_cada_pedido'])}")
#print(f"Mediana de precio cada pedido: {mediana(df['precio_cada_pedido'])}")
#print(f"Desviación estándar de precio cada pedido: {desviacion_estandar(df['precio_cada_pedido'])}")

#calcular la media, mediana y desviación estandar de la columna ventas
#print(f"Media de ventas: {media(df['ventas'])}")
#print(f"Mediana de ventas: {mediana(df['ventas'])}")
#print(f"Desviación estándar de ventas: {desviacion_estandar(df['ventas'])}")

#calcular la media, mediana y desviación estandar de la columna precio_venta_sugerido
#print(f"Media de precio venta sugerido: {media(df['precio_venta_sugerido'])}")
#print(f"Mediana de precio venta sugerido: {mediana(df['precio_venta_sugerido'])}")
#print(f"Desviación estándar de precio venta sugerido: {desviacion_estandar(df['precio_venta_sugerido'])}")

#Teniendo en cuenta que hay disntintos tipos de productos que se venden tiene sentido calcular la los estadísticos de cada producto
#Para esto se puede crear una función que reciba como parámetro el nombre del producto y la columna y calcule los estadísticos
#def estadisticos_producto(producto, columna):
    print(f"Media de {producto}: {media(df[df['linea_producto'] == producto][columna])}")
    print(f"Mediana de {producto}: {mediana(df[df['linea_producto'] == producto][columna])}")
    print(f"Desviación estándar de {producto}: {desviacion_estandar(df[df['linea_producto'] == producto][columna])}")

#Mirar que productos hay que variables aparecen en linea_producto
#print(df['linea_producto'].unique())

#Calcular los estadísticos para cada producto en ventas
#estadisticos_producto('Classic Cars', 'ventas')
#estadisticos_producto('Motorcycles', 'ventas')
#estadisticos_producto('Planes', 'ventas')
#estadisticos_producto('Ships', 'ventas')
#estadisticos_producto('Trains', 'ventas')
#estadisticos_producto('Trucks and Buses', 'ventas')
#estadisticos_producto('Vintage Cars', 'ventas')






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