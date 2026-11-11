from .reglas import REGLAS
from .motor_sugeno import evaluar

DATOS_HOJAS = {"R1": (50, 0), "R2": (46, 1), "R3": (48, 1), "R4": (3, 0), "R5": (3, 1)}

def confianzas() -> dict[str, float]:
    return {regla: correctos/(correctos+incorrectos) for regla, (correctos, incorrectos) in DATOS_HOJAS.items()}

def evaluar_con_confianza(ancho: float, largo: float):
    return evaluar(ancho, largo, ponderar_confianza=True)
