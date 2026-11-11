import matplotlib.pyplot as plt
from .estrella import LINEAS, sumas_lineas

# Coordenadas correspondientes al esquema clásico de estrella de David.
# Intersecciones de seis rectas (tres direcciones, dos triángulos). Cada
# cromosoma de estrella.py asigna sus doce posiciones A–L a estos cruces.
COORDENADAS = ((-3, 0), (2.5, .5), (3, 0), (0, 3), (1, 2), (2, 0),
               (-1, 2), (-4, 0), (-1, -3), (-6, 2), (-3.5, -.5), (4, 2))
ETIQUETAS = tuple("ABCDEFGHIJKL")

def dibujar_estrella(ax, individuo, titulo=None):
    sumas = sumas_lineas(individuo)
    for n, linea in enumerate(LINEAS):
        puntos = sorted((COORDENADAS[i] for i in linea), key=lambda p: p[0])
        xs = [p[0] for p in puntos]; ys = [p[1] for p in puntos]
        error = abs(sumas[n] - 26)
        color = "#18864b" if error == 0 else "#cc3d3d"
        ax.plot(xs, ys, linewidth=2.5, color=color,
                label=f"L{n+1}: {sumas[n]} (error {error})", zorder=1)
    for indice, ((x, y), valor) in enumerate(zip(COORDENADAS, individuo)):
        ax.scatter([x], [y], s=800, color="#fff3cd", edgecolor="#202020", zorder=3)
        ax.text(x, y, str(valor), ha="center", va="center", fontsize=14, weight="bold", zorder=4)
        ax.annotate(ETIQUETAS[indice], (x, y), xytext=(0, 15), textcoords="offset points",
                    ha="center", fontsize=9, weight="bold", color="#333333", zorder=5)
    valida = all(s == 26 for s in sumas)
    fitness_total = sum(abs(s-26) for s in sumas)
    ax.set_title(titulo or f"Estrella mágica — {'válida' if valida else 'no válida'} (fitness {fitness_total})")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.04), ncol=3, fontsize=9)
    ax.set_aspect("equal"); ax.axis("off")
    return sumas, fitness_total

def graficar(individuo, ruta="resultados/estrella.png", mostrar=False):
    fig, ax = plt.subplots(figsize=(7, 7))
    dibujar_estrella(ax, individuo)
    fig.tight_layout(); fig.savefig(ruta, dpi=160, bbox_inches="tight")
    if mostrar: plt.show()
    plt.close(fig); return ruta
