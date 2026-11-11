import matplotlib.pyplot as plt
from .estrella import LINEAS, sumas_lineas

# Coordenadas correspondientes al esquema clásico de estrella de David.
# Cada familia de líneas paralelas tiene una dirección distinta; sus doce
# intersecciones reproducen la incidencia indicada en LINEAS.
COORDENADAS = ((-1, 0), (2, 1), (3, 0), (1, 2), (-1, 4), (1, 0),
               (3, 4), (-2, 0), (-.5, -1.5), (-6, 4), (-1.5, -.5), (5, 4))

def graficar(individuo, ruta="resultados/estrella.png", mostrar=False):
    sumas = sumas_lineas(individuo); fig, ax = plt.subplots(figsize=(7, 7))
    for n, linea in enumerate(LINEAS):
        puntos = sorted((COORDENADAS[i] for i in linea), key=lambda p: p[0])
        xs = [p[0] for p in puntos]; ys = [p[1] for p in puntos]
        ax.plot(xs, ys, linewidth=2, label=f"L{n+1} = {sumas[n]}")
    for (x, y), valor in zip(COORDENADAS, individuo):
        ax.scatter([x], [y], s=900, color="#fff3cd", edgecolor="#202020", zorder=3)
        ax.text(x, y, str(valor), ha="center", va="center", fontsize=14, weight="bold", zorder=4)
    valida = all(s == 26 for s in sumas)
    ax.set_title(f"Estrella mágica — {'válida' if valida else 'no válida'} (fitness {sum(abs(s-26) for s in sumas)})")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.04), ncol=3); ax.set_aspect("equal"); ax.axis("off")
    fig.tight_layout(); fig.savefig(ruta, dpi=160, bbox_inches="tight")
    if mostrar: plt.show()
    plt.close(fig); return ruta
