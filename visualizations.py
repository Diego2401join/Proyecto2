import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

graficas_dir = "resultados/graficas"
os.makedirs(graficas_dir, exist_ok=True)

def generar_graficas(df):
    print("\n📈 Generando gráficas...")

    columnas_numericas = df.select_dtypes(include='number').columns
    if len(columnas_numericas) < 2:
        print("No hay suficientes columnas numéricas para graficar.")
        return

    plt.figure(figsize=(8, 5))
    sns.histplot(df[columnas_numericas[0]], kde=True)
    plt.title(f"Histograma de {columnas_numericas[0]}")
    plt.savefig(f"{graficas_dir}/histograma_{columnas_numericas[0]}.png")
    plt.close()

    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df[columnas_numericas])
    plt.title("Boxplot de variables numéricas")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"{graficas_dir}/boxplot_numericas.png")
    plt.close()

    plt.figure(figsize=(10, 8))
    corr = df[columnas_numericas].corr()
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Mapa de calor de correlaciones")
    plt.tight_layout()
    plt.savefig(f"{graficas_dir}/heatmap_correlaciones.png")
    plt.close()

    if len(columnas_numericas) >= 2:
        plt.figure(figsize=(8, 6))
        sns.scatterplot(data=df, x=columnas_numericas[0], y=columnas_numericas[1])
        plt.title(f"Scatterplot entre {columnas_numericas[0]} y {columnas_numericas[1]}")
        plt.savefig(f"{graficas_dir}/scatter_{columnas_numericas[0]}_{columnas_numericas[1]}.png")
        plt.close()

    print(f"Gráficas guardadas en {graficas_dir}/ ✅")
