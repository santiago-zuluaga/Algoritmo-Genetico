from collections.abc import Sequence

NUMEROS = tuple(range(1, 13))
LINEAS = ((0, 2, 5, 7), (0, 3, 6, 10), (1, 2, 3, 4),
          (1, 5, 8, 11), (4, 6, 9, 11), (7, 8, 9, 10))

def validar_individuo(individuo: Sequence[int]) -> bool:
    return len(individuo) == 12 and sorted(individuo) == list(NUMEROS)

def sumas_lineas(individuo: Sequence[int]) -> tuple[int, ...]:
    if not validar_individuo(individuo): raise ValueError("El cromosoma debe ser una permutación de 1..12.")
    return tuple(sum(individuo[i] for i in linea) for linea in LINEAS)

def fitness(individuo: Sequence[int], objetivo: int = 26) -> int:
    return sum(abs(suma - objetivo) for suma in sumas_lineas(individuo))
