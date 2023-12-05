import pandas as pd

archivo = 'Auto_Sales_data.csv'
data = pd.read_csv(archivo)

#Filtramos las filas donde QUANTITYORDERED >50
condicion_filtrado = data['QUANTITYORDERED'] > 50

# Aplicar el filtrado utilizando la función loc
datos_filtrados = data.loc[condicion_filtrado]
print(datos_filtrados)


# Verifica los nombres de las columnas en tu DataFrame
print(data.columns)

# Agreguemos una nueva columna llamada 'Estado' basada en las ventas anuales
for indice, fila in data.iterrows():
    if 'Ventas_Anuales' in data.columns and fila['Ventas_Anuales'] > 10000:
        data.at[indice, 'Estado'] = 'Alto'
    elif 'Ventas_Anuales' in data.columns and 5000 <= fila['Ventas_Anuales'] <= 10000:
        data.at[indice, 'Estado'] = 'Moderado'
    else:
        data.at[indice, 'Estado'] = 'Bajo'

# Imprime el DataFrame modificado
print(data)