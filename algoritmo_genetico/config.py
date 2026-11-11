from dataclasses import dataclass

@dataclass(frozen=True)
class ConfiguracionAG:
    tamano_poblacion: int = 100
    max_generaciones: int = 1000
    probabilidad_mutacion: float = 0.15
    elitismo: int = 2
    tamano_torneo: int = 3
    semilla: int | None = 42

    def __post_init__(self):
        if self.tamano_poblacion < 2: raise ValueError("La población debe ser al menos 2.")
        if self.max_generaciones < 0: raise ValueError("Las generaciones no pueden ser negativas.")
        if not 0 <= self.probabilidad_mutacion <= 1: raise ValueError("La mutación debe estar entre 0 y 1.")
        if not 0 <= self.elitismo < self.tamano_poblacion: raise ValueError("El elitismo debe ser menor que la población.")
        if not 1 <= self.tamano_torneo <= self.tamano_poblacion: raise ValueError("Torneo fuera de rango.")
