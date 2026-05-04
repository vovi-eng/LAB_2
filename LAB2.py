import pandas as pd
 
 
df_ev      = pd.read_csv("Electric_Vehicle_Population-2.csv")
df_gym     = pd.read_csv("GymExerciseTracking.csv")
df_steam   = pd.read_csv("steam_store_data_2024.csv")
df_netflix = pd.read_csv("netflix_titles.csv")
 
# Limpieza de columnas Steam: convertir precio y descuento a numérico
df_steam["precio_num"]    = df_steam["price"].str.replace("$", "", regex=False).astype(float)
df_steam["descuento_num"] = (
    pd.to_numeric(df_steam["salePercentage"].str.replace("%", "", regex=False), errors="coerce")
    .abs()
    .fillna(0)
    .astype(int)
)
 
# Limpieza Netflix: extraer año de date_added y minutos de duration
df_netflix["anio_agregado"] = pd.to_datetime(
    df_netflix["date_added"].str.strip(), format="%B %d, %Y", errors="coerce"
).dt.year
 
df_netflix["duracion_min"] = df_netflix["duration"].str.extract(r"(\d+) min").astype(float)
 
def explorar_dataset(nombre, df):
    separador = "=" * 60
    print(f"\n{separador}")
    print(f"  DATASET: {nombre}")
    print(separador)
 
    filas, columnas = df.shape
    print(f"\n  Filas: {filas}  |  Columnas: {columnas}")
 
    print(f"\n  Columnas:")
    for columna in df.columns:
        print(f"    - {columna}")
 
    print(f"\n  Primeras 6 filas:")
    print(df.head(6).to_string(index=False))
 
    print(f"\n  Estadísticas de variables numéricas:")
    print(df.describe().to_string())
 
 
explorar_dataset("Vehículos Eléctricos", df_ev)
explorar_dataset("Seguimiento de Gimnasio", df_gym)
explorar_dataset("Steam Store 2024",       df_steam)
explorar_dataset("Netflix Títulos",        df_netflix)
 
