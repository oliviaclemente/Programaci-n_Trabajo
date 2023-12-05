import pandas as pd

# Cargamos los datos
df = pd.read_csv('Auto_Sales_data.csv')

# 1. Margen de Ganancia
df['Margen_Ganancia'] = (df['SALES'] - (df['QUANTITYORDERED'] * df['PRICEEACH'])) / df['SALES']

# 2. Categoría de Ventas
def categorizar_ventas(sales):
    if sales < 5000:
        return 'Pequeña'
    elif sales < 20000:
        return 'Mediana'
    else:
        return 'Grande'

df['Categoria_Ventas'] = df['SALES'].apply(categorizar_ventas)

# 3. Tiempo desde la Última Compra
def clasificar_tiempo(dias):
    if dias <= 30:
        return 'Reciente'
    elif dias <= 90:
        return 'Moderado'
    else:
        return 'Distante'
    
df['Clasificacion_Compra'] = df['DAYS_SINCE_LASTORDER'].apply(clasificar_tiempo)

# 4. Prioridad de Cliente (Ejemplo simple)
# Esto podría ser más complejo si acumulamos datos por cliente
df['Prioridad_Cliente'] = df['SALES'].apply(lambda x: 'Alta' if x > 10000 else ('Media' if x > 5000 else 'Baja'))

# 5. Estado de Pedido
def estado_pedido(status):
    if status in ['Shipped', 'Resolved']:
        return 'Completado'
    elif status in ['In Process', 'On Hold']:
        return 'En Proceso'
    else:
        return 'Retrasado'

df['Estado_Pedido'] = df['STATUS'].apply(estado_pedido)

# Guardamos los cambios
df.to_csv('Auto_Sales_data_modificado.csv', index=False)