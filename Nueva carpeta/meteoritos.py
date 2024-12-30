import pandas as pd
from geopy.geocoders import Nominatim
from tqdm import tqdm

# Cargar el dataset limpio
meteoritos = pd.read_csv("c:/Users/claud/Downloads/meteoritos_limpio.csv")

# Inicializar el geocodificador
geolocator = Nominatim(user_agent="geoapi")

# Ordenar por ID en forma decreciente
meteoritos = meteoritos.sort_values(by="id", ascending=False)

# Mostrar la cantidad de registros
total_registros = len(meteoritos)
print(f"Cantidad total de registros: {total_registros}")

# Seleccionar un rango de registros
inicio = 0  # Cambia este valor para seleccionar el rango de inicio (ej. 1500)
fin = 30  # Cambia este valor para el rango final (ej. 3000)
sub_meteoritos = meteoritos.iloc[inicio:fin]

# Crear una función para obtener el código de país
def obtener_country_code(lat, lon):
    try:
        location = geolocator.reverse((lat, lon), language="en")
        return location.raw["address"]["country_code"]
    except:
        return "NA"

# Aplicar la función a los registros seleccionados
tqdm.pandas()
sub_meteoritos.loc[:, "country_code"] = sub_meteoritos.progress_apply(
    lambda row: obtener_country_code(row["lat"], row["long"]), axis=1
)

# Crear una lista de tuplas con (id, country_code)
lista_tuplas = list(zip(sub_meteoritos["id"], sub_meteoritos["country_code"]))

# Guardar la lista de tuplas en un archivo de texto
with open("lista_tuplas.txt", "w") as file:
    for tupla in lista_tuplas:
        file.write(f"{tupla}\n")

print(f"Archivo 'lista_tuplas.txt' creado con {len(lista_tuplas)} registros.")
