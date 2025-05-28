import pandas as pd
from scipy import stats
import numpy as np

def generar_estadisticas(df):
    """Genera estadísticas descriptivas básicas del DataFrame."""
    print("\n📊 Generando estadísticas descriptivas...")
    resumen = df.describe(include='all')
    print(resumen)
    return resumen

def realizar_pruebas_estadisticas(df):
    """Realiza pruebas estadísticas básicas entre variables numéricas."""
    print("\n🧪 Realizando pruebas estadísticas básicas...")

    resultados = []
    columnas_numericas = df.select_dtypes(include=np.number).columns

    for i, col1 in enumerate(columnas_numericas):
        for col2 in columnas_numericas[i+1:]:
            try:
                r, p = stats.pearsonr(df[col1], df[col2])
                resultados.append({
                    'var1': col1,
                    'var2': col2,
                    'correlacion_pearson': r,
                    'p_valor': p
                })
            except Exception as e:
                print(f"Error correlacionando {col1} y {col2}: {e}")

    resultados_df = pd.DataFrame(resultados)
    print(resultados_df.head())
    return resultados_df
