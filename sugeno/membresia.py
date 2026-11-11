from dataclasses import dataclass

def triangular(x: float, a: float, b: float, c: float) -> float:
    if not a <= b <= c: raise ValueError("Se requiere a <= b <= c.")
    if x < a or x > c: return 0.0
    if x == b: return 1.0
    if x < b: return 1.0 if a == b else (x-a)/(b-a)
    return 1.0 if b == c else (c-x)/(c-b)

def trapezoidal(x: float, a: float, b: float, c: float, d: float) -> float:
    if not a <= b <= c <= d: raise ValueError("Se requiere a <= b <= c <= d.")
    if x < a or x > d: return 0.0
    if b <= x <= c: return 1.0
    if x < b: return 1.0 if a == b else (x-a)/(b-a)
    return 1.0 if c == d else (d-x)/(d-c)

@dataclass(frozen=True)
class ConjuntosIris:
    """Transiciones en cm; solapamiento suave alrededor de límites del enunciado."""
    ancho_small: tuple = (-0.2, 0.0, 0.55, 0.75)
    ancho_medium: tuple = (0.45, 0.75, 1.4, 1.65)
    ancho_large: tuple = (1.35, 1.65, 3.0, 3.0)
    largo_small: tuple = (-1.0, 0.0, 1.8, 2.2)
    largo_medium: tuple = (1.8, 2.2, 4.7, 5.1)
    largo_large: tuple = (4.7, 5.1, 8.0, 8.0)

    def evaluar(self, variable: str, x: float) -> dict[str, float]:
        conjuntos = {"petalwidth": (self.ancho_small, self.ancho_medium, self.ancho_large),
                     "petallength": (self.largo_small, self.largo_medium, self.largo_large)}
        if variable not in conjuntos: raise ValueError(f"Variable desconocida: {variable}")
        return dict(zip(("small", "medium", "large"), (trapezoidal(x, *p) for p in conjuntos[variable])))

def rampa_mayor(x: float, limite: float, ancho: float = .2) -> float:
    inicio, fin = limite-ancho/2, limite+ancho/2
    if x <= inicio + 1e-12: return 0.0
    if x >= fin - 1e-12: return 1.0
    return (x-inicio)/ancho

def rampa_menor_igual(x: float, limite: float, ancho: float = .2) -> float:
    return 1.0 - rampa_mayor(x, limite, ancho)
