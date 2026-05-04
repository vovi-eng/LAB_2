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
print("\n" + "=" * 60)
print("  SECCIÓN 2 – INGRESO DE NUEVOS DATOS")
print("=" * 60)
 

print("\n  Ingrese los datos del nuevo vehículo eléctrico:")
 
nuevo_vin       = input("    VIN (primeros 10 caracteres): ").strip()
nueva_ciudad    = input("    Ciudad: ").strip()
nuevo_anio      = int(input("    Año del modelo (2000-2025): "))
nueva_marca     = input("    Marca (Make): ").strip().upper()
nuevo_modelo    = input("    Modelo: ").strip().upper()
nuevo_tipo_ev   = input("    Tipo EV (Battery Electric Vehicle (BEV) / Plug-in Hybrid Electric Vehicle (PHEV)): ").strip()
nueva_elegib    = input("    Elegibilidad CAFV: ").strip()
nuevo_rango     = int(input("    Rango eléctrico (millas): "))
nuevo_msrp      = int(input("    Precio base MSRP ($): "))
nueva_utilidad  = input("    Empresa de electricidad: ").strip()
 
nuevo_registro_ev = {
    "VIN (1-10)":            nuevo_vin,
    "City":                  nueva_ciudad,
    "Model Year":            nuevo_anio,
    "Make":                  nueva_marca,
    "Model":                 nuevo_modelo,
    "Electric_Vehicle_Type": nuevo_tipo_ev,
    "CAFV_Eligibility":      nueva_elegib,
    "Electric_Range":        nuevo_rango,
    "Base_MSRP":             nuevo_msrp,
    "Electric Utility":      nueva_utilidad,
}
 
df_ev = pd.concat([df_ev, pd.DataFrame([nuevo_registro_ev])], ignore_index=True)
print(f"\n  Registro añadido. Total de vehículos ahora: {len(df_ev):,}")
 
print("\n  Ingrese los datos de la nueva sesión de gimnasio:")
 
nueva_edad        = int(input("    Edad: "))
nuevo_genero      = input("    Género (Male/Female): ").strip()
nuevo_peso        = float(input("    Peso (kg): "))
nueva_altura      = float(input("    Altura (m): "))
nuevo_max_bpm     = int(input("    BPM máximo: "))
nuevo_avg_bpm     = int(input("    BPM promedio: "))
nuevo_rest_bpm    = int(input("    BPM en reposo: "))
nueva_duracion    = float(input("    Duración de sesión (horas): "))
nuevas_calorias   = float(input("    Calorías quemadas: "))
nuevo_tipo_ej     = input("    Tipo de ejercicio (Yoga/HIIT/Cardio/Strength): ").strip()
nuevo_grasa       = float(input("    Porcentaje de grasa corporal: "))
nuevo_agua        = float(input("    Ingesta de agua (litros): "))
nueva_frecuencia  = int(input("    Frecuencia de entrenamiento (días/semana): "))
nuevo_nivel       = int(input("    Nivel de experiencia (1/2/3): "))
nuevo_bmi         = float(input("    IMC: "))
 
nuevo_registro_gym = {
    "Age":                          nueva_edad,
    "Gender":                       nuevo_genero,
    "Weight (kg)":                  nuevo_peso,
    "Height (m)":                   nueva_altura,
    "Max_BPM":                      nuevo_max_bpm,
    "Avg_BPM":                      nuevo_avg_bpm,
    "Resting_BPM":                  nuevo_rest_bpm,
    "Session_Duration (hours)":     nueva_duracion,
    "Calories_Burned":              nuevas_calorias,
    "Workout_Type":                 nuevo_tipo_ej,
    "Fat_Percentage":               nuevo_grasa,
    "Water_Intake (liters)":        nuevo_agua,
    "Workout_Frequency (days/week)": nueva_frecuencia,
    "Experience_Level":             nuevo_nivel,
    "BMI":                          nuevo_bmi,
}
 
df_gym = pd.concat([df_gym, pd.DataFrame([nuevo_registro_gym])], ignore_index=True)
print(f"\n  Registro añadido. Total de sesiones ahora: {len(df_gym):,}")