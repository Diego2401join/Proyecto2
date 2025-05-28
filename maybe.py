import argparse
import os

from data_loader import cargar_datos, limpiar_datos
from stadisticas import generar_estadisticas, realizar_pruebas_estadisticas
from visualizations import generar_graficas
from utils import temporizador, exportar_resumen
from edo_solver import resolver_edo

@temporizador
def pipeline(ruta_csv):
    df = cargar_datos(ruta_csv)
    df = limpiar_datos(df)
    resumen_stats = generar_estadisticas(df)
    resultados_pruebas = realizar_pruebas_estadisticas(df)
    generar_graficas(df)
    exportar_resumen(resumen_stats, resultados_pruebas)

if __name__ == "__main__":
    print("🧪 Proyecto de análisis en Python")
    print("1. Analizar archivo CSV")
    print("2. Resolver ecuación diferencial")
    opcion = input("Seleccione una opción (1 o 2): ")

    if opcion == "1":
        ruta = input("📂 Ingrese la ruta del archivo CSV (Enter para usar el default): ").strip()
        if not ruta:
            ruta = "datos/historical-weather-medellin (1).csv"
        if not os.path.exists(ruta):
            print(f"❌ No se encontró el archivo: {ruta}")
        else:
            pipeline(ruta)
    elif opcion == "2":
        resolver_edo()
    else:
        print("❌ Opción no válida.")
