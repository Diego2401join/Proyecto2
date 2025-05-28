import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def resolver_edo():
    print("\n📐 Resolviendo ecuación diferencial: dy/dt = -2y, y(0)=1")

    def modelo(t, y):
        return -2 * y

    t_span = (0, 5)
    y0 = [1]

    solucion = solve_ivp(modelo, t_span, y0, t_eval=np.linspace(t_span[0], t_span[1], 100))

    plt.plot(solucion.t, solucion.y[0], label="y(t)")
    plt.title("Solución de la EDO: dy/dt = -2y")
    plt.xlabel("t")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()

    # Crear carpeta resultados si no existe
    import os
    os.makedirs("resultados", exist_ok=True)
    plt.savefig("resultados/edo_solucion.png")
    plt.close()

    print("✅ Solución graficada y guardada en resultados/edo_solucion.png")
