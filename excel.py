import os
import pandas as pd

# Ruta de la carpeta que contiene los archivos CSV
carpeta_csv = "c:/Users/claud/Desktop/Nueva carpeta (2)"

# Crear una lista vacía para almacenar los DataFrames
dataframes = []

# Iterar sobre todos los archivos en la carpeta
for archivo in os.listdir(carpeta_csv):
    if archivo.endswith(".csv"):  # Filtrar solo los archivos CSV
        ruta_archivo = os.path.join(carpeta_csv, archivo)
        # Leer el archivo CSV y añadirlo a la lista
        df = pd.read_csv(ruta_archivo)
        dataframes.append(df)

# Combinar todos los DataFrames en uno solo
df_combinado = pd.concat(dataframes, ignore_index=True)

# Eliminar las columnas 'lat' y 'long'
df_combinado = df_combinado.drop(columns=['lat', 'long'])

# Renombrar 'country_name' a 'country_id'
df_combinado = df_combinado.rename(columns={'country_name': 'country_id'})

# Eliminar las filas con valores NA
df_combinado = df_combinado.dropna()

# Guardar el DataFrame combinado en un nuevo archivo CSV
archivo_salida = "c:/Users/claud/Desktop/archivo_combinado.csv"
df_combinado.to_csv(archivo_salida, index=False)

print(f"Archivo combinado y procesado guardado en: {archivo_salida}")
