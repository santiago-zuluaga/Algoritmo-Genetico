import random
from algoritmo_genetico.config import ConfiguracionAG
from algoritmo_genetico.estrella import LINEAS, fitness, sumas_lineas, validar_individuo
from algoritmo_genetico.genetico import (crear_individuo, cruce_ox, cruce_ox_detallado,
    mutacion_swap, mutacion_swap_detallada, seleccion_torneo, ejecutar, ejecutar_con_historial)
from algoritmo_genetico.visualizacion import COORDENADAS, graficar

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
    hijos, (i, j), detalle = cruce_ox_detallado(p[0], p[1], random.Random(4))
    assert validar_individuo(hijos[0]) and len(detalle['segmento']) == j-i+1
    mutado, indices = mutacion_swap_detallada(p[0], random.Random(5))
    assert validar_individuo(mutado) and len(indices) == 2
    r = ejecutar(ConfiguracionAG(30, 20, .15, 2, 3, 9))
    assert validar_individuo(r.mejor_individuo) and isinstance(r.generaciones, int)

def test_historial_de_generaciones():
    datos = ejecutar_con_historial(ConfiguracionAG(20, 5, .15, 2, 3, 8))
    assert datos.estadisticas[0].generacion == 0
    assert datos.estadisticas[-1].generacion == datos.resultado.generaciones
    assert all(0 <= x.diversidad <= 1 for x in datos.estadisticas)

def test_visualizacion(tmp_path):
    ruta = tmp_path / "estrella.png"; graficar(REFERENCIA, str(ruta)); assert ruta.exists()

def test_geometria_representa_las_seis_lineas():
    for indices in LINEAS:
        p0, p1 = (COORDENADAS[i] for i in indices[:2])
        dx, dy = p1[0]-p0[0], p1[1]-p0[1]
        for indice in indices[2:]:
            x, y = COORDENADAS[indice]
            assert abs(dx*(y-p0[1]) - dy*(x-p0[0])) < 1e-9
