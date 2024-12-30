import pandas as pd

# Leer el archivo CSV
archivo_csv = "C:/Users/claud/Desktop/Nueva carpeta (2)/archivo_combinado.csv"
df = pd.read_csv(archivo_csv)

# Convertir el DataFrame en una lista de listas (cada fila es una sublista)
lista_combinado = df.values.tolist()

# Crear el formato adecuado para R
r_lista = "lista_combinado <- list(\n"
for fila in lista_combinado:
    r_lista += "  c(" + ", ".join(map(str, fila)) + "),\n"
r_lista += ")"

# Mostrar el código de la lista en formato R
print(r_lista)

# Guardar el código en un archivo de texto (opcional)
with open("C:/Users/claud/Desktop/Nueva carpeta (2)/codigo_r_archivo_combinado.R", "w") as f:
    f.write(r_lista)

print("Código guardado en: C:/Users/claud/Desktop/Nueva carpeta (2)/codigo_r_archivo_combinado.R")
