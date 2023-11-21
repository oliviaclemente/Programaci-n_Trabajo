import numpy as np
import pandas as pd


archivo = 'R.csv'
data = pd.read_csv(archivo)  # Utiliza pd.read_csv() para cargar los datos desde un archivo CSV

primeras = data.head()
ultimas = data.tail()

# Imprime las primeras y las últimas filas
print(f"Primeras filas: {primeras}")
print(f"Últimas 5 filas: {ultimas}")
