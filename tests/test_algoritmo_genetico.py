import random
from algoritmo_genetico.config import ConfiguracionAG
from algoritmo_genetico.estrella import fitness, sumas_lineas, validar_individuo
from algoritmo_genetico.genetico import crear_individuo, cruce_ox, mutacion_swap, seleccion_torneo, ejecutar
from algoritmo_genetico.visualizacion import graficar

REFERENCIA = [1, 5, 6, 12, 3, 10, 11, 9, 7, 8, 2, 4]

def test_individuo_y_referencia():
    assert validar_individuo(crear_individuo(random.Random(1)))
    assert sumas_lineas(REFERENCIA) == (26, 26, 26, 26, 26, 26)
    assert fitness(REFERENCIA) == 0

def test_operadores_y_resultado():
    rng = random.Random(2); p = [crear_individuo(rng) for _ in range(8)]
    assert seleccion_torneo(p, 3, rng) in p
    for h in cruce_ox(p[0], p[1], rng): assert validar_individuo(h)
    assert validar_individuo(mutacion_swap(p[0], rng))
    r = ejecutar(ConfiguracionAG(30, 20, .15, 2, 3, 9))
    assert validar_individuo(r.mejor_individuo) and isinstance(r.generaciones, int)

def test_visualizacion(tmp_path):
    ruta = tmp_path / "estrella.png"; graficar(REFERENCIA, str(ruta)); assert ruta.exists()
