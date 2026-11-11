from dataclasses import dataclass
from .membresia import rampa_mayor, rampa_menor_igual

CONSECUENTES = {"Iris-setosa": 0.0, "Iris-versicolor": 1.0, "Iris-virginica": 2.0}

@dataclass(frozen=True)
class Regla:
    id: str
    clase: str
    confianza: float

    @property
    def consecuente(self): return CONSECUENTES[self.clase]

REGLAS = (Regla("R1", "Iris-setosa", 1.0), Regla("R2", "Iris-virginica", 46/47),
          Regla("R3", "Iris-versicolor", 48/49), Regla("R4", "Iris-virginica", 1.0),
          Regla("R5", "Iris-versicolor", 3/4))

def activaciones(ancho: float, largo: float) -> dict[str, float]:
    gt06 = rampa_mayor(ancho, .6); le06 = 1-gt06
    gt17 = rampa_mayor(ancho, 1.7); le17 = 1-gt17
    le49 = rampa_menor_igual(largo, 4.9); gt49 = 1-le49
    le15 = rampa_menor_igual(ancho, 1.5); gt15 = 1-le15
    return {"R1": le06, "R2": min(gt06, gt17), "R3": min(gt06, le17, le49),
            "R4": min(gt06, le17, gt49, le15), "R5": min(gt06, le17, gt49, gt15)}
