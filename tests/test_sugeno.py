import pytest
from sugeno.membresia import ConjuntosIris, triangular, trapezoidal
from sugeno.motor_sugeno import evaluar, promedio_ponderado
from sugeno.reglas import activaciones

def test_membresias_en_rangos_y_limites():
    mf = ConjuntosIris()
    for x in (.6, 1.5, 2.0, 4.9):
        for v in (mf.evaluar("petalwidth", x) if x < 2 else mf.evaluar("petallength", x)).values():
            assert 0 <= v <= 1
    assert triangular(1, 0, 1, 2) == 1
    assert trapezoidal(.5, 0, .5, 1, 2) == 1

def test_reglas_ejemplo_obligatorio():
    r = evaluar(1.6, 5.0)
    assert r.grados["petalwidth"]["medium"] > 0
    assert all(0 <= v <= 1 for v in r.activaciones.values())
    assert r.consecuentes == {"R1": 0., "R2": 2., "R3": 1., "R4": 2., "R5": 1.}
    assert r.salida == pytest.approx(1.0)
    assert r.clasificacion == "Iris-versicolor"

def test_sin_reglas_activas():
    assert promedio_ponderado({"R1": 0.0}, {"R1": 0.0}) is None
    assert activaciones(10, -10)["R2"] == 1
