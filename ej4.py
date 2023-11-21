import numpy as np
import pandas as pd

archivo = 'Auto_Sales_data.csv'
data = pd.read_csv(archivo)  # Utiliza pd.read_csv() para cargar los datos desde un archivo CSV

if 'ORDERNUMBER' in data.columns:
    media_order_number = data['ORDERNUMBER'].mean() # Calcula la media de 'ORDERNUMBER'
    filas_superiores = data[data['ORDERNUMBER'] > media_order_number]

    print(f'Media de ORDERNUMBER: {media_order_number}')

    if not filas_superiores.empty:
        print(f'Número de filas que superan la media: {len(filas_superiores)}')
    else:
        print('No hay filas que superen la media.')
else:
    print('La columna "ORDERNUMBER" no está presente en el DataFrame.')