import numpy as np
import pandas as pd

# Cargar datos desde el archivo CSV
archivo = 'Auto_Sales_data.csv'
data = pd.read_csv(archivo)

# Función para reemplazar NaN con la moda o la media
def replace_nan(df, column, method='mean'):
    if df[column].isnull().sum() > 0:
        if method == 'mean':
            df[column].fillna(df[column].mean(), inplace=True)
        elif method == 'mode':
            df[column].fillna(df[column].mode()[0], inplace=True)

# Aplicar la función a todas las columnas
for column in data.columns:
    replace_nan(data, column)

# Tratar valores fuera de 2 desviaciones estándar
for column in data.select_dtypes(include=[np.number]).columns:
    mean = data[column].mean()
    std = data[column].std()
    upper_bound = mean + 2*std
    lower_bound = mean - 2*std
    data[column] = np.where((data[column] > upper_bound) | (data[column] < lower_bound), data[column].mean(), data[column])

# Convertir tipos de datos si es necesario

# Renombrar columnas
data.columns = ['columna_' + str(i) for i in range(1, len(data.columns)+1)]

# Imprimir estadísticas básicas de las columnas numéricas
for column in data.select_dtypes(include=[np.number]).columns:
    print(f"\nEstadísticas de la columna {column}:")
    print(f"Media: {data[column].mean()}")
    print(f"Mediana: {data[column].median()}")
    print(f"Desviación Estándar: {data[column].std()}")

# Crear gráficos para visualizar la distribución de los datos
for column in data.select_dtypes(include=[np.number]).columns:
    plt.figure(figsize=(10, 6))
    sns.histplot(data=data, x=column, kde=True)
    plt.title(f'Distribución de {column}')
    plt.show()

# Filtrar el dataset utilizando condiciones específicas
filtered_data = data[data['columna_1'] > 100]

# Crear nuevas columnas aplicando funciones o cálculos basados en valores de otras columnas
data['nueva_columna'] = data['columna_2'] * 2

# Utilizar bucles para iterar sobre filas o columnas y realizar cálculos
for index, row in data.iterrows():
    data.at[index, 'nueva_columna_2'] = row['columna_3'] / 2

# Imprimir el DataFrame después de las manipulaciones
print(data.head())
