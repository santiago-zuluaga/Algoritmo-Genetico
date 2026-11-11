import random
from dataclasses import dataclass
from .config import ConfiguracionAG
from .estrella import NUMEROS, fitness, validar_individuo

Individuo = list[int]

@dataclass
class ResultadoAG:
    mejor_individuo: Individuo
    mejor_fitness: int
    generaciones: int
    encontrado: bool

@dataclass
class EstadisticasGeneracion:
    generacion: int
    mejor_fitness: int
    fitness_promedio: float
    peor_fitness: int
    diversidad: float
    mejor_individuo: Individuo

@dataclass
class HistorialAG:
    resultado: ResultadoAG
    estadisticas: list[EstadisticasGeneracion]

def _resumir(poblacion: list[Individuo], generacion: int) -> EstadisticasGeneracion:
    valores = [fitness(ind) for ind in poblacion]
    mejor = min(range(len(poblacion)), key=valores.__getitem__)
    return EstadisticasGeneracion(
        generacion, valores[mejor], sum(valores) / len(valores), max(valores),
        len({tuple(ind) for ind in poblacion}) / len(poblacion), poblacion[mejor].copy()
    )

def crear_individuo(rng: random.Random) -> Individuo:
    individuo = list(NUMEROS); rng.shuffle(individuo); return individuo

def seleccion_torneo(poblacion: list[Individuo], tamano: int, rng: random.Random) -> Individuo:
    return min(rng.sample(poblacion, tamano), key=fitness)

def cruce_ox(padre1: Individuo, padre2: Individuo, rng: random.Random) -> tuple[Individuo, Individuo]:
    """Order crossover: conserva un segmento y rellena respetando el orden del otro padre."""
    hijos, _, _ = cruce_ox_detallado(padre1, padre2, rng)
    return hijos

def cruce_ox_detallado(padre1: Individuo, padre2: Individuo, rng: random.Random):
    """Versión didáctica de OX: hijos, corte inclusivo y pasos de relleno."""
    if not validar_individuo(padre1) or not validar_individuo(padre2): raise ValueError("Padres inválidos.")
    i, j = sorted(rng.sample(range(len(padre1)), 2))
    def hijo(a, b):
        result = [None] * len(a)
        result[i:j+1] = a[i:j+1]
        restante = [g for g in b[j+1:] + b[:j+1] if g not in result]
        posiciones = list(range(j+1, len(a))) + list(range(0, i))
        for pos, gen in zip(posiciones, restante): result[pos] = gen
        return result, {"segmento": a[i:j+1], "relleno": restante,
                        "pasos": list(zip(posiciones, restante))}
    hijo1, detalle = hijo(padre1, padre2)
    hijo2, _ = hijo(padre2, padre1)
    return (hijo1, hijo2), (i, j), detalle

def mutacion_swap(individuo: Individuo, rng: random.Random, probabilidad: float = 1.0) -> Individuo:
    hijo, _ = mutacion_swap_detallada(individuo, rng, probabilidad)
    return hijo

def mutacion_swap_detallada(individuo: Individuo, rng: random.Random, probabilidad: float = 1.0):
    resultado = individuo.copy()
    posiciones = None
    if rng.random() < probabilidad:
        i, j = rng.sample(range(len(resultado)), 2); posiciones = (i, j)
        resultado[i], resultado[j] = resultado[j], resultado[i]
    return resultado, posiciones

def avanzar_poblacion(poblacion: list[Individuo], config: ConfiguracionAG, rng: random.Random) -> list[Individuo]:
    """Construye una generación aplicando elitismo, torneo, OX y swap."""
    ordenados = sorted(poblacion, key=fitness)
    nueva = [x.copy() for x in ordenados[:config.elitismo]]
    while len(nueva) < config.tamano_poblacion:
        p1 = seleccion_torneo(poblacion, config.tamano_torneo, rng)
        p2 = seleccion_torneo(poblacion, config.tamano_torneo, rng)
        for hijo in cruce_ox(p1, p2, rng):
            nueva.append(mutacion_swap(hijo, rng, config.probabilidad_mutacion))
            if len(nueva) == config.tamano_poblacion: break
    return nueva

def ejecutar_con_historial(config: ConfiguracionAG = ConfiguracionAG()) -> HistorialAG:
    rng = random.Random(config.semilla)
    poblacion = [crear_individuo(rng) for _ in range(config.tamano_poblacion)]
    mejor = min(poblacion, key=fitness); mejor_f = fitness(mejor); hechas = 0
    historial = [_resumir(poblacion, 0)]
    if mejor_f == 0: return HistorialAG(ResultadoAG(mejor, mejor_f, 0, True), historial)
    for generacion in range(1, config.max_generaciones + 1):
        poblacion = avanzar_poblacion(poblacion, config, rng); hechas = generacion
        candidato = min(poblacion, key=fitness); valor = fitness(candidato)
        historial.append(_resumir(poblacion, generacion))
        if valor < mejor_f: mejor, mejor_f = candidato.copy(), valor
        if valor == 0: return HistorialAG(ResultadoAG(candidato, 0, hechas, True), historial)
    return HistorialAG(ResultadoAG(mejor, mejor_f, hechas, mejor_f == 0), historial)

def ejecutar(config: ConfiguracionAG = ConfiguracionAG()) -> ResultadoAG:
    """Interfaz sencilla compatible con versiones anteriores del proyecto."""
    return ejecutar_con_historial(config).resultado
