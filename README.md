
# 📘 README – Análisis de Datos Climáticos de Medellín

## 🔍 Descripción
Este proyecto en Python realiza un análisis automatizado de datos climáticos históricos de Medellín. Además, incluye una herramienta para resolver una ecuación diferencial ordinaria simple.

## 🧱 Estructura del Proyecto

```
├── data_loader.py              # Carga y limpieza de datos
├── edo_solver.py              # Solución de EDO (dy/dt = -2y)
├── historical-weather-medellin.csv  # Dataset principal
├── main.py                    # Versión por línea de comandos
├── maybe.py                   # Interfaz por consola con menú
├── stadisticas.py             # Estadísticas y pruebas estadísticas
├── utils.py                   # Utilidades y funciones de exportación
├── visualizations.py          # Generación de gráficas
├── resultados/                # Carpeta generada automáticamente con resultados
```

## ⚙️ Requisitos

- Python 3.7 o superior
- Bibliotecas:
  ```bash
  pip install pandas numpy scipy matplotlib seaborn
  ```

## 🚀 Uso

### Opción 1: Ejecutar con menú interactivo
```bash
python maybe.py
```
Se presentará un menú:
```
1. Analizar archivo CSV
2. Resolver ecuación diferencial
```

### Opción 2: Ejecutar análisis desde la línea de comandos
```bash
python main.py --csv historical-weather-medellin.csv
```

## 📊 Funcionalidades

1. **Carga y limpieza del CSV**
   - Elimina columnas/filas vacías
   - Rellena valores numéricos faltantes con la media
   - Elimina duplicados

2. **Estadísticas**
   - Estadísticas descriptivas
   - Pruebas de correlación (Pearson)

3. **Visualizaciones**
   - Histograma
   - Boxplot
   - Heatmap de correlación
   - Scatterplot

4. **Exportación**
   - Resultados exportados a la carpeta `resultados/` con timestamp

5. **Ecuación Diferencial**
   - Solución de `dy/dt = -2y` con condición inicial `y(0) = 1`
   - Gráfico exportado a `resultados/edo_solucion.png`

## 📁 Resultados
Todos los resultados (CSV y gráficas) se guardan en la carpeta `resultados/`.

## 👨‍💻 Autor
*Proyecto desarrollado como ejemplo de análisis automatizado de datos climáticos y solución de EDO.*

