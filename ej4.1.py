import pandas as pd

archivo = 'Nuevo_archivo.csv'
data = pd.read_csv(archivo)

#Filtramos las filas donde QUANTITYORDERED >50
condicion_filtrado = data['QUANTITYORDERED'] > 50

# Aplicar el filtrado utilizando la función loc
datos_filtrados = data.loc[condicion_filtrado]
print(datos_filtrados)

