'''Limpieza y preprocesamiento de datos:
• Identifiquen y traten o imputen los valores faltantes NaN usando una 
función personalizada que use la moda/media para remplazarlos. En 
caso de no haber filas con NaN, todo dato que esté por encima o por 
debajo de dos desviaciones típicas de la media tendrá que imputarse 
por la moda/media.
• Conviertan los tipos de datos de las columnas si es necesario.
• Renombren las columnas para facilitar su manipulación.'''

import pandas as pd
import numpy as np

archivo = 'Auto_Sales_data.csv'
df = pd.read_csv(archivo)  # Utiliza pd.read_csv() para cargar los datos desde un archivo CSV

# Función para reemplazar NaN con la moda o la media
def replace_nan(df, column, method='mean'):
    if df[column].isnull().sum() > 0:
        if method == 'mean':
            df[column].fillna(df[column].mean(), inplace=True)
        elif method == 'mode':
            df[column].fillna(df[column].mode()[0], inplace=True)

# Aplicar la función a todas las columnas
for column in df.columns:
    replace_nan(df, column)

# Tratar valores fuera de 2 desviaciones estándar
for column in df.select_dtypes(include=[np.number]).columns:
    mean = df[column].mean()
    std = df[column].std()
    upper_bound = mean + 2*std
    lower_bound = mean - 2*std
    df[column] = np.where((df[column] > upper_bound) | (df[column] < lower_bound), df[column].mean(), df[column])
    
print(df)

# Convertir tipos de datos si es necesario

# Renombrar columnas

df.columns = ['columna_' + str(i) for i in range(1, len(df.columns)+1)]
print(df.columns)