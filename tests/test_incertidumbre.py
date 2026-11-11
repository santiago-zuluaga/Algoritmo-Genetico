import pytest
from sugeno.incertidumbre import confianzas, evaluar_con_confianza

def test_confianzas():
    c = confianzas(); assert c["R1"] == 1 and c["R2"] == pytest.approx(46/47)
    assert c["R5"] == .75

def test_evaluacion_ponderada_ejemplo():
    r = evaluar_con_confianza(1.6, 5.0)
    assert r.salida is not None and r.activaciones["R5"] > 0
    assert r.clasificacion == "Iris-versicolor"
