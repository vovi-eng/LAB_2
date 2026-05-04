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



print("\n" + "=" * 60)
print("  SECCIÓN 3 – FILTRADO DE DATOS")
print("=" * 60)

print("\n  [Vehículos Eléctricos] Filtro 1: año de modelo anterior al ingresado")
anio_filtro = int(input("    Ingrese el año límite (2000-2025): "))
resultado_ev_anio = df_ev[df_ev["Model Year"] < anio_filtro]
print(f"    Vehículos con año de modelo antes de {anio_filtro}: {len(resultado_ev_anio):,}")
print(resultado_ev_anio[["VIN (1-10)", "Make", "Model", "Model Year"]].head(10).to_string(index=False))

print("\n  [Vehículos Eléctricos] Filtro 2: precio base inferior al ingresado")
precio_filtro = float(input("    Ingrese el precio máximo ($0.00 - $845,000.00): "))
resultado_ev_precio = df_ev[df_ev["Base_MSRP"] < precio_filtro]
print(f"    Vehículos con precio base menor a ${precio_filtro:,.2f}: {len(resultado_ev_precio):,}")
print(resultado_ev_precio[["VIN (1-10)", "Make", "Model", "Base_MSRP"]].head(10).to_string(index=False))

print("\n  [Gimnasio] Filtro 1: calorías quemadas mayor o igual al ingresado")
calorias_filtro = float(input("    Ingrese el mínimo de calorías quemadas (mín: 0.0): "))
resultado_gym_cal = df_gym[df_gym["Calories_Burned"] >= calorias_filtro]
print(f"    Sesiones con al menos {calorias_filtro} kcal: {len(resultado_gym_cal):,}")
print(resultado_gym_cal[["Age", "Gender", "Workout_Type", "Calories_Burned"]].head(10).to_string(index=False))

print("\n  [Gimnasio] Filtro 2: porcentaje de grasa menor o igual al ingresado")
grasa_filtro = float(input("    Ingrese el porcentaje máximo de grasa (0.0% - 100.0%): "))
resultado_gym_grasa = df_gym[df_gym["Fat_Percentage"] <= grasa_filtro]
print(f"    Sesiones con grasa corporal <= {grasa_filtro}%: {len(resultado_gym_grasa):,}")
print(resultado_gym_grasa[["Age", "Gender", "Workout_Type", "Fat_Percentage"]].head(10).to_string(index=False))


print("\n  [Videojuegos] Filtro 1: precio superior al ingresado")
precio_steam_filtro = float(input("    Ingrese el precio mínimo ($): "))
resultado_steam_precio = df_steam[df_steam["precio_num"] > precio_steam_filtro]
print(f"    Juegos con precio mayor a ${precio_steam_filtro:.2f}: {len(resultado_steam_precio):,}")
print(resultado_steam_precio[["title", "price", "allReviews"]].head(10).to_string(index=False))

print("\n  [Videojuegos] Filtro 2: porcentaje de descuento menor al ingresado")
descuento_filtro = int(input("    Ingrese el descuento máximo (%): "))
resultado_steam_desc = df_steam[df_steam["descuento_num"] < descuento_filtro]
print(f"    Juegos con descuento menor a {descuento_filtro}%: {len(resultado_steam_desc):,}")
print(resultado_steam_desc[["title", "salePercentage", "price"]].head(10).to_string(index=False))

print("\n  [Netflix] Filtro 1: películas con duración mayor a los minutos ingresados")
min_filtro = float(input("    Ingrese el mínimo de minutos de duración: "))
resultado_netflix_dur = df_netflix[
    (df_netflix["type"] == "Movie") & (df_netflix["duracion_min"] > min_filtro)
]
print(f"    Películas con duración mayor a {min_filtro} minutos: {len(resultado_netflix_dur):,}")
print(resultado_netflix_dur[["title", "duration", "rating"]].head(10).to_string(index=False))

print("\n  [Netflix] Filtro 2: contenido añadido antes del año ingresado")
anio_netflix_filtro = int(input("    Ingrese el año límite: "))
resultado_netflix_anio = df_netflix[df_netflix["anio_agregado"] < anio_netflix_filtro]
print(f"    Títulos añadidos antes de {anio_netflix_filtro}: {len(resultado_netflix_anio):,}")
print(resultado_netflix_anio[["title", "type", "date_added"]].head(10).to_string(index=False))


print("\n" + "=" * 60)
print("  SECCIÓN 4 – EXPLORACIÓN AVANZADA")
print("=" * 60)

def clasificar_rango_ev(rango):
    if rango < 100:
        return "Bajo"
    if rango <= 250:
        return "Medio"
    return "Alto"

df_ev["RangoCategoria"] = df_ev["Electric_Range"].apply(clasificar_rango_ev)

# Gimnasio: NivelFrecuencia
def clasificar_frecuencia_gym(frecuencia):
    if frecuencia < 3:
        return "Baja"
    if frecuencia <= 5:
        return "Moderada"
    return "Alta"

df_gym["NivelFrecuencia"] = df_gym["Workout_Frequency (days/week)"].apply(clasificar_frecuencia_gym)

# Videojuegos: GamaJuego
def clasificar_gama_steam(precio):
    if precio < 10:
        return "Baja"
    if precio <= 24:
        return "Media"
    return "Alta"

df_steam["GamaJuego"] = df_steam["precio_num"].apply(clasificar_gama_steam)

clasificacion_audiencia = {
    "G":        "Niños",
    "TV-Y":     "Niños",
    "TV-G":     "Niños",
    "TV-Y7":    "Niños",
    "TV-Y7-FV": "Niños",
    "PG":       "Adolescentes",
    "TV-PG":    "Adolescentes",
    "PG-13":    "Adultos Jóvenes",
    "TV-14":    "Adultos Jóvenes",
    "R":        "Adultos",
    "TV-MA":    "Adultos",
    "NC-17":    "Adultos",
}

df_netflix["TipoAudiencia"] = df_netflix["rating"].map(clasificacion_audiencia).fillna("Sin clasificar")

print("\n  Variables categóricas creadas correctamente en los cuatro datasets.")


print("\n  Conteo por categoría – Vehículos Eléctricos (RangoCategoria):")
print(df_ev["RangoCategoria"].value_counts().to_string())

print("\n  Conteo por categoría – Gimnasio (NivelFrecuencia):")
print(df_gym["NivelFrecuencia"].value_counts().to_string())

print("\n  Conteo por categoría – Videojuegos (GamaJuego):")
print(df_steam["GamaJuego"].value_counts().to_string())

print("\n  Conteo por categoría – Netflix (TipoAudiencia):")
print(df_netflix["TipoAudiencia"].value_counts().to_string())

conteo_ev = df_ev["RangoCategoria"].value_counts().reindex(["Bajo", "Medio", "Alto"])
grafico_ev = conteo_ev.plot(
    kind="bar",
    title="Vehículos Eléctricos – Categoría de rango eléctrico",
    color=["#4C72B0", "#55A868", "#C44E52"],
    rot=0,
)
grafico_ev.set_xlabel("Categoría de rango")
grafico_ev.set_ylabel("Cantidad de vehículos")
grafico_ev.get_figure().tight_layout()
grafico_ev.get_figure().savefig("grafico_ev.png", dpi=150)
grafico_ev.get_figure().show()

# Gráfico 2: Gimnasio
conteo_gym = df_gym["NivelFrecuencia"].value_counts().reindex(["Baja", "Moderada", "Alta"])
grafico_gym = conteo_gym.plot(
    kind="bar",
    title="Gimnasio – Nivel de frecuencia de entrenamiento",
    color=["#4C72B0", "#55A868", "#C44E52"],
    rot=0,
)
grafico_gym.set_xlabel("Nivel de frecuencia")
grafico_gym.set_ylabel("Cantidad de sesiones")
grafico_gym.get_figure().tight_layout()
grafico_gym.get_figure().savefig("grafico_gym.png", dpi=150)
grafico_gym.get_figure().show()

# Gráfico 3: Steam
conteo_steam = df_steam["GamaJuego"].value_counts().reindex(["Baja", "Media", "Alta"])
grafico_steam = conteo_steam.plot(
    kind="bar",
    title="Videojuegos Steam – Gama de precio",
    color=["#4C72B0", "#55A868", "#C44E52"],
    rot=0,
)
grafico_steam.set_xlabel("Gama de precio")
grafico_steam.set_ylabel("Cantidad de juegos")
grafico_steam.get_figure().tight_layout()
grafico_steam.get_figure().savefig("grafico_steam.png", dpi=150)
grafico_steam.get_figure().show()

# Gráfico 4: Netflix
orden_audiencia = ["Niños", "Adolescentes", "Adultos Jóvenes", "Adultos", "Sin clasificar"]
conteo_netflix = df_netflix["TipoAudiencia"].value_counts().reindex(orden_audiencia).dropna()
grafico_netflix = conteo_netflix.plot(
    kind="bar",
    title="Netflix – Tipo de audiencia",
    color=["#4C72B0", "#55A868", "#C44E52", "#8172B2", "#CCB974"],
    rot=15,
)
grafico_netflix.set_xlabel("Audiencia")
grafico_netflix.set_ylabel("Cantidad de títulos")
grafico_netflix.get_figure().tight_layout()
grafico_netflix.get_figure().savefig("grafico_netflix.png", dpi=150)
grafico_netflix.get_figure().show()

print("\n  Gráficos guardados: grafico_ev.png, grafico_gym.png, grafico_steam.png, grafico_netflix.png")


print("\n  Análisis agrupado – Vehículos Eléctricos:")
agrupado_ev = df_ev.groupby("RangoCategoria").agg(
    media_MSRP=("Base_MSRP", "mean"),
    media_anio=("Model Year", "mean"),
    std_rango=("Electric_Range", "std"),
).round(2)
print(agrupado_ev.to_string())

print("\n  Análisis agrupado – Gimnasio:")
agrupado_gym = df_gym.groupby("NivelFrecuencia").agg(
    media_duracion=("Session_Duration (hours)", "mean"),
    media_experiencia=("Experience_Level", "mean"),
    std_bmi=("BMI", "std"),
).round(2)
print(agrupado_gym.to_string())

print("\n  Análisis agrupado – Videojuegos:")
agrupado_steam = df_steam.groupby("GamaJuego").agg(
    media_precio=("precio_num", "mean"),
    media_descuento=("descuento_num", "mean"),
    std_precio=("precio_num", "std"),
).round(2)
print(agrupado_steam.to_string())

print("\n  Análisis agrupado – Netflix (tipo más común y duración promedio por audiencia):")
agrupado_netflix = df_netflix.groupby("TipoAudiencia").agg(
    tipo_mas_comun=("type", lambda columna: columna.mode()[0] if not columna.empty else "N/A"),
    duracion_promedio_min=("duracion_min", "mean"),
).round(2)
print(agrupado_netflix.to_string())


print("\n" + "=" * 60)
print("  SECCIÓN 5 – PREGUNTAS CLAVE")
print("=" * 60)

print("\n  P1-EV: ¿Los vehículos con mayor rango pertenecen a modelos más recientes?")

correlacion_rango_anio = df_ev[["Electric_Range", "Model Year"]].corr().iloc[0, 1]
media_rango_por_anio = df_ev.groupby("Model Year")["Electric_Range"].mean().tail(10)

print(f"  Correlación Electric_Range vs Model Year: {correlacion_rango_anio:.4f}")
print("  Media de rango por año (últimos 10 años registrados):")
print(media_rango_por_anio.to_string())
print("  Respuesta: La correlación positiva indica que los modelos más recientes tienden")
print("  a tener mayor rango eléctrico, aunque la relación no es perfectamente lineal.")

print("\n  P2-EV: ¿Los vehículos con mayor precio base tienen mayor rango eléctrico?")

df_ev_con_precio = df_ev[df_ev["Base_MSRP"] > 0]
correlacion_precio_rango = df_ev_con_precio[["Base_MSRP", "Electric_Range"]].corr().iloc[0, 1]
media_rango_por_precio = (
    df_ev_con_precio
    .assign(tramo_precio=pd.cut(df_ev_con_precio["Base_MSRP"], bins=4, labels=["Bajo", "Medio", "Alto", "Premium"]))
    .groupby("tramo_precio")["Electric_Range"]
    .mean()
    .round(2)
)

print(f"  Correlación Base_MSRP vs Electric_Range (excluyendo MSRP=0): {correlacion_precio_rango:.4f}")
print("  Media de rango por tramo de precio:")
print(media_rango_por_precio.to_string())
print("  Respuesta: La correlación sugiere una relación débil/moderada. Los vehículos")
print("  de mayor precio no siempre tienen el mayor rango; el dataset contiene muchos")
print("  registros con MSRP en cero (datos no reportados) que afectan el análisis.")

print("\n  P1-GYM: ¿Mayor duración de sesión implica más calorías quemadas?")

correlacion_dur_cal = df_gym[["Session_Duration (hours)", "Calories_Burned"]].corr().iloc[0, 1]
media_cal_por_duracion = (
    df_gym
    .assign(tramo_dur=pd.cut(df_gym["Session_Duration (hours)"], bins=4, labels=["Corta", "Media", "Larga", "Muy larga"]))
    .groupby("tramo_dur")["Calories_Burned"]
    .mean()
    .round(2)
)

print(f"  Correlación Session_Duration vs Calories_Burned: {correlacion_dur_cal:.4f}")
print("  Media de calorías por tramo de duración:")
print(media_cal_por_duracion.to_string())
print("  Respuesta: La correlación fuerte positiva confirma que las sesiones más largas")
print("  queman significativamente más calorías.")

print("\n  P2-GYM: ¿Menor grasa corporal implica mayor nivel de experiencia?")

correlacion_grasa_exp = df_gym[["Fat_Percentage", "Experience_Level"]].corr().iloc[0, 1]
media_grasa_por_nivel = df_gym.groupby("Experience_Level")["Fat_Percentage"].mean().round(2)

print(f"  Correlación Fat_Percentage vs Experience_Level: {correlacion_grasa_exp:.4f}")
print("  Media de grasa corporal por nivel de experiencia:")
print(media_grasa_por_nivel.to_string())
print("  Respuesta: La correlación negativa indica que los usuarios con mayor nivel de")
print("  experiencia tienden a tener menor porcentaje de grasa corporal.")

print("\n  P1-STEAM: ¿Los juegos de gama alta tienen mejores calificaciones?")

orden_reviews = {
    "Overwhelmingly Positive": 5,
    "Very Positive": 4,
    "Mostly Positive": 3,
    "Mixed": 2,
    "Mostly Negative": 1,
    "Overwhelmingly Negative": 0,
}
df_steam["puntaje_review"] = df_steam["allReviews"].map(orden_reviews)
media_review_por_gama = df_steam.groupby("GamaJuego")["puntaje_review"].mean().round(2)
conteo_reviews_por_gama = df_steam.groupby(["GamaJuego", "allReviews"]).size().unstack(fill_value=0)

print("  Puntaje promedio de reviews por gama (5=Abrumadoramente positivo, 1=Negativo):")
print(media_review_por_gama.to_string())
print("  Respuesta: Los datos muestran si la gama alta tiene mejor calificación promedio.")
print("  Consulte el puntaje para determinar la tendencia exacta.")

print("\n  P2-STEAM: ¿Cuál es el rango de precios de los juegos mejor calificados?")

df_steam_top = df_steam[df_steam["allReviews"] == "Overwhelmingly Positive"]
if not df_steam_top.empty:
    precio_min_top = df_steam_top["precio_num"].min()
    precio_max_top = df_steam_top["precio_num"].max()
    precio_med_top = df_steam_top["precio_num"].mean()
    print(f"  Juegos 'Overwhelmingly Positive': {len(df_steam_top)}")
    print(f"    Precio mínimo: ${precio_min_top:.2f}")
    print(f"    Precio máximo: ${precio_max_top:.2f}")
    print(f"    Precio promedio: ${precio_med_top:.2f}")
else:
    print("  No hay juegos con calificación 'Overwhelmingly Positive' en la muestra.")

print("\n  P1-NETFLIX: ¿Cuáles son los 10 títulos más recientes añadidos al catálogo?")

df_netflix["fecha_completa"] = pd.to_datetime(
    df_netflix["date_added"].str.strip(), format="%B %d, %Y", errors="coerce"
)
top10_recientes = (
    df_netflix
    .dropna(subset=["fecha_completa"])
    .nlargest(10, "fecha_completa")
    [["title", "type", "date_added", "country"]]
)
print(top10_recientes.to_string(index=False))

print("\n  P2-NETFLIX: ¿Cuáles son los países con más producciones?")

conteo_paises = (
    df_netflix["country"]
    .dropna()
    .str.split(", ")
    .explode()
    .str.strip()
    .value_counts()
    .head(10)
)
print(conteo_paises.to_string())



print("\n" + "=" * 60)
print("  SECCIÓN 6 – GUARDADO DE RESULTADOS")
print("=" * 60)

df_ev.drop(columns=["RangoCategoria"], errors="ignore")
df_ev.to_csv("Electric_Vehicle_Population_Actualizado.csv", index=False)

df_gym.to_csv("GymExerciseTracking_Actualizado.csv", index=False)

df_steam.to_csv("steam_store_data_2024_Actualizado.csv", index=False)

df_netflix.drop(columns=["fecha_completa"], errors="ignore")
df_netflix.to_csv("netflix_titles_Actualizado.csv", index=False)

print("\n  Archivos guardados:")
print("    Electric_Vehicle_Population_Actualizado.csv")
print("    GymExerciseTracking_Actualizado.csv")
print("    steam_store_data_2024_Actualizado.csv")
print("    netflix_titles_Actualizado.csv")
print("\n  El programa ha finalizado correctamente.")