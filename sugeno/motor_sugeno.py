from dataclasses import dataclass
from .membresia import ConjuntosIris
from .reglas import REGLAS, activaciones

NOMBRES = ("Iris-setosa", "Iris-versicolor", "Iris-virginica")

@dataclass
class ResultadoSugeno:
    grados: dict
    activaciones: dict
    consecuentes: dict
    salida: float | None
    clasificacion: str | None

def clase_desde_salida(z: float | None) -> str | None:
    if z is None: return None
    # El número de clase más cercano; los empates se asignan a la clase de índice menor.
    indice = max(0, min(2, int(z + .5 - 1e-12)))
    return NOMBRES[indice]

def promedio_ponderado(pesos: dict, consecuentes: dict) -> float | None:
    denominador = sum(pesos.values())
    if denominador == 0: return None
    return sum(peso * consecuentes[nombre] for nombre, peso in pesos.items()) / denominador

def evaluar(ancho: float, largo: float, ponderar_confianza: bool = False) -> ResultadoSugeno:
    mf = ConjuntosIris()
    grados = {"petalwidth": mf.evaluar("petalwidth", ancho), "petallength": mf.evaluar("petallength", largo)}
    activ = activaciones(ancho, largo)
    pesos = {r.id: activ[r.id] * (r.confianza if ponderar_confianza else 1.0) for r in REGLAS}
    consecuentes = {r.id: r.consecuente for r in REGLAS}
    salida = promedio_ponderado(pesos, consecuentes)
    return ResultadoSugeno(grados, pesos, consecuentes, salida, clase_desde_salida(salida))
