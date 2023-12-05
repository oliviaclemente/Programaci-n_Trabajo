import pandas as pd

# Leer el archivo CSV
archivo = 'Auto_Sales_data.csv'
data = pd.read_csv(archivo)

# Ejemplo 1: Crear una nueva columna que sea la suma de dos columnas existentes
data['Nueva_Columna'] = data['Columna1'] + data['Columna2']

# Ejemplo 2: Crear una nueva columna que sea el producto de dos columnas existentes
data['Otra_Nueva_Columna'] = data['Columna3'] * data['Columna4']

# Ejemplo 3: Aplicar una función a una columna existente para crear una nueva columna
def calcular_nueva_columna(valor):
    return valor * 2

data['Columna_Nueva'] = data['Columna_Existente'].apply(calcular_nueva_columna)

# Ejemplo 4: Crear una nueva columna basada en una condición
data['Nueva_Columna_Condicional'] = np.where(data['Columna_Condicional'] > 10, 'Mayor', 'Menor')

# Puedes seguir combinando funciones y operaciones según tus necesidades.

# Guardar el DataFrame modificado en un nuevo archivo CSV
data.to_csv('Nuevo_Archivo.csv', index=False)
