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

def crear_individuo(rng: random.Random) -> Individuo:
    individuo = list(NUMEROS); rng.shuffle(individuo); return individuo

def seleccion_torneo(poblacion: list[Individuo], tamano: int, rng: random.Random) -> Individuo:
    return min(rng.sample(poblacion, tamano), key=fitness)

def cruce_ox(padre1: Individuo, padre2: Individuo, rng: random.Random) -> tuple[Individuo, Individuo]:
    """Order crossover: conserva un segmento y rellena respetando el orden del otro padre."""
    if not validar_individuo(padre1) or not validar_individuo(padre2): raise ValueError("Padres inválidos.")
    def hijo(a, b):
        i, j = sorted(rng.sample(range(len(a)), 2)); result = [None] * len(a)
        result[i:j+1] = a[i:j+1]
        restante = [g for g in b[j+1:] + b[:j+1] if g not in result]
        posiciones = list(range(j+1, len(a))) + list(range(0, i))
        for pos, gen in zip(posiciones, restante): result[pos] = gen
        return result
    return hijo(padre1, padre2), hijo(padre2, padre1)

def mutacion_swap(individuo: Individuo, rng: random.Random, probabilidad: float = 1.0) -> Individuo:
    resultado = individuo.copy()
    if rng.random() < probabilidad:
        i, j = rng.sample(range(len(resultado)), 2); resultado[i], resultado[j] = resultado[j], resultado[i]
    return resultado

def ejecutar(config: ConfiguracionAG = ConfiguracionAG()) -> ResultadoAG:
    rng = random.Random(config.semilla)
    poblacion = [crear_individuo(rng) for _ in range(config.tamano_poblacion)]
    mejor = min(poblacion, key=fitness); mejor_f = fitness(mejor); hechas = 0
    if mejor_f == 0: return ResultadoAG(mejor, mejor_f, 0, True)
    for generacion in range(1, config.max_generaciones + 1):
        ordenados = sorted(poblacion, key=fitness)
        nueva = [x.copy() for x in ordenados[:config.elitismo]]
        while len(nueva) < config.tamano_poblacion:
            p1 = seleccion_torneo(poblacion, config.tamano_torneo, rng)
            p2 = seleccion_torneo(poblacion, config.tamano_torneo, rng)
            for hijo in cruce_ox(p1, p2, rng):
                nueva.append(mutacion_swap(hijo, rng, config.probabilidad_mutacion))
                if len(nueva) == config.tamano_poblacion: break
        poblacion = nueva; hechas = generacion
        candidato = min(poblacion, key=fitness); valor = fitness(candidato)
        if valor < mejor_f: mejor, mejor_f = candidato.copy(), valor
        if valor == 0: return ResultadoAG(candidato, 0, hechas, True)
    return ResultadoAG(mejor, mejor_f, hechas, mejor_f == 0)
