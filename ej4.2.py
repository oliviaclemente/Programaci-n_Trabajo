import pandas as pd

archivo = 'Auto_Sales_data.csv'
data = pd.read_csv(archivo)

# Iterar sobre columnas
for columna in data.columns:
    # Acceder a los valores de cada fila en la columna actual
    for valor in data[columna]:
        # Realizar cálculos o cualquier operación necesaria
        resultado = valor * 2

        # Puedes imprimir o hacer lo que desees con el resultado
        print(resultado)
