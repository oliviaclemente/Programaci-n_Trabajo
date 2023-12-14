import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv('Auto_Sales_data_modificado.csv')

# Iterar sobre las filas
for index, row in df.iterrows():  #La funcion df.iterrows se utiliza para iterar sobre las filas de un csv
    # Realizar cálculos con los datos de cada fila
    df.at[index, 'NuevaColumna'] = row['QUANTITYORDERED'] * row['PRICEEACH'] #row representa una fila del csv

# Iterar sobre las columnas
for column in df.columns:
    # Realizar cálculos con los datos de cada columna
    if pd.api.types.is_numeric_dtype(df[column]):   #La funcion pd.api.types.is_numeric_dtype se utiliza para verificar si un tipo de datos es numérico
        print(f'Promedio de {column}: {df[column].mean()}')

# Guardar el DataFrame modificado en un nuevo archivo CSV
df.to_csv('Auto_Sales_data_modificado_resultado.csv', index=False)

 #La funcion index=False se ultiliza para guardar el DataFrame en un archivo CSV sin incluir la columna de índices