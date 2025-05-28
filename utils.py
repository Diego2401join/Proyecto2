import os
import time
from functools import wraps
import pandas as pd
from datetime import datetime

def temporizador(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        duracion = fin - inicio
        print(f"⏱️ Tiempo de ejecución: {duracion:.2f} segundos")
        return resultado
    return wrapper

def exportar_resumen(resumen_stats, resultados_pruebas):
    os.makedirs("resultados", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    if isinstance(resumen_stats, pd.DataFrame):
        resumen_stats.to_csv(f"resultados/estadisticas_{timestamp}.csv")

    if isinstance(resultados_pruebas, pd.DataFrame):
        resultados_pruebas.to_csv(f"resultados/pruebas_estadisticas_{timestamp}.csv")

    print("📁 Resultados exportados en la carpeta 'resultados/'")
