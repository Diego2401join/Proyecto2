import argparse
from data_loader import cargar_datos, limpiar_datos
from stadisticas import generar_estadisticas, realizar_pruebas_estadisticas
from visualizations import generar_graficas
from utils import temporizador, exportar_resumen

@temporizador
def pipeline(ruta_csv):
    # Cargar y limpiar datos
    df = cargar_datos(ruta_csv)
    df = limpiar_datos(df)

    # Estadísticas y pruebas
    resumen_stats = generar_estadisticas(df)
    resultados_pruebas = realizar_pruebas_estadisticas(df)

    # Gráficas
    generar_graficas(df)

    # Exportar
    exportar_resumen(resumen_stats, resultados_pruebas)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Análisis automático de CSV de clima.")
    parser.add_argument("--csv", type=str, default="historical-weather-medellin.csv", help="Ruta del archivo CSV")
    args = parser.parse_args()
    pipeline(args.csv)
