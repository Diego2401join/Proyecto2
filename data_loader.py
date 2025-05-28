import pandas as pd
ruta_csv = 'historical-weather-medellin.csv'
def cargar_datos(ruta_csv):
    print("📥 Cargando datos...")
    try:
        df = pd.read_csv(ruta_csv)
        print(f"✅ Datos cargados correctamente. Filas: {len(df)}, Columnas: {len(df.columns)}")
        return df
    except Exception as e:
        print(f"❌ Error al cargar el CSV: {e}")
        raise

def limpiar_datos(df):
    print("🧹 Limpiando datos...")

    # Eliminar columnas completamente vacías
    df = df.dropna(axis=1, how='all')

    # Eliminar filas completamente vacías
    df = df.dropna(axis=0, how='all')

    # Rellenar valores faltantes con la media si son numéricos
    for col in df.select_dtypes(include='number').columns:
        df[col] = df[col].fillna(df[col].mean())

    # Eliminar duplicados si existen
    df = df.drop_duplicates()

    print("✅ Limpieza completada.")
    return df
