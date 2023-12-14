'''Análisis exploratorio de datos (EDA):
• Calculen estadísticas básicas de las columnas numéricas media, 
mediana, desviación estándar usando funciones personalizadas que 
tendréis que crear vosotros.
• Crear gráficos para visualizar la distribución de los datos, como 
histogramas y diagramas de caja.
• Identifiquen y analicen las correlaciones entre variables.
'''


# Aquí no va el código pero en el notebook sí


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

from ej2 import df


# Eliminar columnas que no se utilizarán y separar datos numericos y no numericos
df_num = df.select_dtypes(include=['float64', 'int64']).drop(columns=['numero_del_pedido', 'numero_linea_pedido'])
df_cat = df.select_dtypes(include = ['object']).drop(columns = ['nombre_cliente', 'telefono', 'direccion_linea1', 'codigo_postal', 'apellido_contacto', 'nombre_contacto', 'codigo_producto'])
print(df_num.columns)
print(df_cat.columns)

# Función para calcular la media
def media(columna):
    return sum(columna) / len(columna)

# Función para calcular la mediana
def mediana(columna):
    columna_ordenada = sorted(columna)
    if len(columna) % 2 == 0:
        mediana = (columna_ordenada[int(len(columna) / 2)] + columna_ordenada[int(len(columna) / 2) - 1]) / 2
    else:
        mediana = columna_ordenada[int(len(columna) / 2)]
    return mediana

# Función para calcular la desviación estándar
import math
def desviacion_estandar(columna):
    medias = media(columna)
    squared_diff = [(x - medias)**2 for x in columna]
    variance = sum(squared_diff) / len(columna)
    std_dev = math.sqrt(variance)
    return round(std_dev, 2)

# Calcular los estadísticos
# Estadísticas descriptivas personalizadas
custom_stats = pd.DataFrame({
    'Media': df_num.apply(media),
    'Mediana': df_num.apply(mediana),
    'Desviación Estándar': df_num.apply(desviacion_estandar),
})

# Redondear a dos decimales
custom_stats = custom_stats.round(2)

# Transponer el DataFrame
custom_stats = custom_stats.T

# Mostrar el resultado
print(custom_stats)

#Gráficos para visualizar los datos
sns.pairplot(df.select_dtypes(include=np.number))
plt.grid()
plt.show()

sns.set(style="whitegrid")

# Crear el gráfico de líneas
plt.figure(figsize=(12, 6))
sns.lineplot(data=df_num.groupby('fecha_pedido')['ventas'].sum(), marker='o', color='b', label='Ventas')

# Configuración del título y etiquetas
plt.title('Ventas a lo largo del tiempo', fontsize=16)
plt.xlabel('Fecha de Pedido', fontsize=14)
plt.ylabel('Ventas', fontsize=14)

# Rotar las etiquetas del eje x para una mejor legibilidad
plt.xticks(rotation=45)

# Añadir una leyenda
plt.legend()

# Mostrar la cuadrícula
plt.grid(True, linestyle='--', alpha=0.7)

# Mostrar el gráfico
plt.show()

# Configuración del estilo
sns.set(style="whitegrid")

# Crear el gráfico de líneas con color verde
plt.figure(figsize=(12, 6))
sns.lineplot(data=df_num.groupby('fecha_pedido')['cantidad_de_pedidos'].sum(), marker='o', color='green', label='Ventas')

# Configuración del título y etiquetas
plt.title('Cantidad pedida a lo largo del tiempo', fontsize=16)
plt.xlabel('Fecha de Pedido', fontsize=14)
plt.ylabel('Cantidad', fontsize=14)

# Rotar las etiquetas del eje x para una mejor legibilidad
plt.xticks(rotation=45)

# Añadir una leyenda
plt.legend()

# Mostrar la cuadrícula
plt.grid(True, linestyle='--', alpha=0.7)

# Mostrar el gráfico
plt.show()

# Calcular la media de las ventas por línea de producto
ventas_promedio = df.groupby('linea_producto')['ventas'].mean().sort_values(ascending=False)

# Configurar el estilo del gráfico
plt.style.use('seaborn-darkgrid')

# Crear el gráfico de barras
fig, ax = plt.subplots(figsize=(10, 6))
bar_plot = ax.bar(ventas_promedio.index, ventas_promedio, color=plt.cm.Greens(np.linspace(0, 1, len(ventas_promedio))), edgecolor='black')

# Añadir etiquetas y título
ax.set_title('Ventas Promedio por tipo de Producto', fontsize=16)
ax.set_xlabel('Tipo de producto', fontsize=14)
ax.set_ylabel('Ventas Promedio', fontsize=14)

# Mostrar el gráfico
plt.show()

# Configuración del estilo
sns.set(style="whitegrid")
plt.figure(figsize=(12, 6))  # Ajustar el tamaño de la figura

# Tu código original
df.groupby('linea_producto')['dias_desde_ultimo_pedido'].mean().sort_values(ascending=False).plot(kind='bar', color='skyblue')

# Configuración del gráfico
plt.title('Días desde el Último Pedido por Línea de Producto', fontsize=16)
plt.xlabel('Línea de Producto', fontsize=14)
plt.ylabel('Días Promedio desde el Último Pedido', fontsize=14)
plt.xticks(rotation=45, ha='right', fontsize=12)  # Rotar las etiquetas del eje x
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Mostrar la leyenda y ajustar la posición
plt.legend(['Días Promedio'], loc='upper right')

# Mostrar el gráfico
plt.tight_layout()  # Ajustar el diseño para evitar cortar etiquetas
plt.show()

# Agrupar por ciudad y sumar las ventas
ventas_por_ciudad = df.groupby('ciudad')['ventas'].sum().sort_values(ascending=False)

# Configurar el estilo de seaborn
sns.set(style="whitegrid")

# Crear el gráfico de barras
plt.figure(figsize=(10, 6))  # Ajustar el tamaño del gráfico

# Utilizar un paleta de colores
colores = sns.color_palette("viridis", len(ventas_por_ciudad))

# Crear el gráfico de barras con colores personalizados
ventas_por_ciudad.plot(kind='bar', color=colores)

# Configurar el título y las etiquetas de los ejes
plt.title('Ventas por Ciudad', fontsize=16)
plt.xlabel('Ciudad', fontsize=14)
plt.ylabel('Ventas', fontsize=14)

# Mostrar el gráfico
plt.show()

# Agrupar por país y sumar la cantidad de pedidos
df_agrupado = df.groupby('pais')['cantidad_de_pedidos'].sum().sort_values(ascending=False)

# Configuración del gráfico
plt.figure(figsize=(10, 6))  # Ajustar el tamaño del gráfico
colors = plt.cm.Paired(range(len(df_agrupado)))  # Colores escalados según los valores

# Crear el gráfico de barras
df_agrupado.plot(kind='bar', color=colors)

# Configuración adicional
plt.title('Total de Pedidos por País', fontsize=16)
plt.xlabel('País', fontsize=14)
plt.ylabel('Cantidad de Pedidos', fontsize=14)
plt.xticks(rotation=45, ha='right')  # Rotar las etiquetas del eje x para mayor legibilidad
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Líneas de cuadrícula en el eje y

# Mostrar el gráfico
plt.tight_layout()  # Ajustar el diseño para evitar cortar etiquetas
plt.show()


# Seleccionar columnas categóricas de interés
grupo_1 = df[['status', 'tamaño_acuerdo']]

# Definir función para análisis univariado de categorías
def Analisis_categoria(cols):
    # Imprimir título y separador
    print("_"*60)
    
    # Definir colores para los gráficos
    colors = ['#79a5db', '#e0a580', '#6fab90', '#896ca8', '#ADD8E6']
    
    # Obtener recuento de cada categoría
    recuento = grupo_1[cols].value_counts()
    
    # Gráfico de barras para la distribución de categorías
    fig = px.bar(recuento, x=recuento.index, y=recuento.values, 
                 title=f'Distribución de {cols}', labels={'x': 'Categoria', 'y': 'Cantidad'},
                 color_discrete_sequence=[colors])
    fig.update_layout(width=700)
    fig.update_layout(plot_bgcolor='#ffffff', paper_bgcolor='#ffffff')
    fig.show()
    
    # Gráfico de donut para el porcentaje de cada categoría
    percentage = (recuento / recuento.sum()) * 100
    fig = px.pie(values=percentage, names=recuento.index,
                 labels={'names': 'Categoria', 'values': 'Porcentaje'}, hole=0.5,
                 color_discrete_sequence=colors)
    fig.add_annotation(x=0.5, y=0.5, align="center", xref="paper", yref="paper",
                       showarrow=False, font_size=15, text=f'{cols}')
    fig.update_layout(legend=dict(x=0.9, y=0.5))
    fig.update_layout(width=700)
    fig.show()
    
    # Imprimir espacio en blanco para separar resultados
    print("       ")

# Iterar sobre las columnas categóricas y realizar análisis univariado
for x in grupo_1:
    Analisis_categoria(x)

#Identifiquen y analicen las correlaciones entre variables
#calcular el coeficiente de relación de Pearson para ver la correlación lineal
corr = df_num.corr(method='pearson')

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

# Datos de precios Y ventas
PRICEEACH = df['precio_cada_pedido'].values
SALES = df['ventas'].values

pendiente, ordenada_al_origen = np.polyfit(PRICEEACH, SALES, 1)
#np.polyfit se utiliza para calcular directamente la pendiente y la ordenada al origen de la recta de regresión

# Imprimir los coeficientes
print(f"Pendiente: {pendiente}")
print(f"Ordenada_al_origen: {ordenada_al_origen}")

# Visualizar los datos y la recta de regresión
plt.scatter(PRICEEACH, SALES, label='Datos reales')
plt.plot(PRICEEACH, pendiente * PRICEEACH + ordenada_al_origen, color='red', label='Recta de regresión')
plt.xlabel('precio de cada pedido')
plt.ylabel('ventas')
plt.legend()
plt.show()
