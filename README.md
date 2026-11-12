# Parcial de Inteligencia Artificial: AG y Sugeno

Proyecto académico con dos módulos independientes: un algoritmo genético que busca una distribución para la estrella mágica de 12 números y un clasificador difuso de flores Iris basado en Sugeno de orden cero.

## Objetivos y estructura

`algoritmo_genetico/` contiene la representación, operadores, ejecución y gráfica. `sugeno/` contiene funciones de pertenencia, reglas, motor Sugeno y ponderación por confianza. `tests/` contiene pruebas pytest, `notebooks/` guías ejecutables en Google Colab y `docs/` el desarrollo matemático.

## Requisitos e instalación

Python 3.11 o superior. Instala dependencias con `python -m pip install -r requirements.txt`.

## Ejecución

```bash
python -m algoritmo_genetico.main
python -m algoritmo_genetico.main --semilla 123 --poblacion 150 --generaciones 1500
python -m sugeno.main
python -m sugeno.main --petalwidth 1.6 --petallength 5.0
```

El primer comando informa el mejor individuo y escribe `resultados/estrella.png`. Cada corrida empieza con una población aleatoria; la solución de referencia del parcial aparece únicamente en pruebas: `[1, 5, 6, 12, 3, 10, 11, 9, 7, 8, 2, 4]`.

## Laboratorio interactivo en Google Colab

Abre el [laboratorio de la estrella mágica en Google Colab](https://colab.research.google.com/github/santiago-zuluaga/Algoritmo-Genetico/blob/main/notebooks/algoritmo_genetico.ipynb). El cuaderno clona este repositorio, presenta los conceptos y operadores en el orden de una clase práctica, permite cambiar parámetros con controles interactivos, inspeccionar generaciones paso a paso y comparar corridas reproducibles. También incluye una animación acotada y gráficas de fitness y diversidad.

Para estudiar el clasificador difuso, abre el [laboratorio del sistema Sugeno para Iris en Google Colab](https://colab.research.google.com/github/santiago-zuluaga/Algoritmo-Genetico/blob/main/notebooks/sistema_sugeno.ipynb). Incluye la implementación visible de pertenencias, reglas, motor Sugeno y ponderación por confianza, además de evaluación y visualizaciones.

## Algoritmo genético

Cada cromosoma es una permutación de 1..12. Se minimiza la suma de desviaciones absolutas de las seis líneas respecto de 26. La selección es por torneo; el cruce OX conserva permutaciones; la mutación intercambia dos genes; el elitismo preserva los mejores. Los parámetros y semilla se configuran por argumentos de terminal. El método es estocástico y no promete convergencia en un número fijo de generaciones.

## Sugeno e incertidumbre

Las entradas son ancho y largo del pétalo. Conjuntos trapezoidales con transiciones solapadas suavizan los límites lingüísticos. Las cinco reglas respetan el árbol, incluidos los umbrales 1.7 y 1.5 en sus respectivas condiciones. MIN combina antecedentes; el promedio ponderado de consecuentes (0, 1, 2) produce una salida continua. Se asigna a la clase cuyo número sea más cercano, desempate hacia el menor. La segunda evaluación multiplica activaciones por la confianza de la hoja (aciertos/total), según `docs/sistema_sugeno.md`.

El ejemplo obligatorio se ejecuta con `python -m sugeno.main`. El resultado se imprime con pertenencias, activaciones/pesos, consecuentes y clasificación; no se presupone una precisión sobre el conjunto Iris completo.

## Pruebas

Ejecuta `python -m pytest -q`. Las pruebas cubren permutaciones, fitness de referencia, operadores, gráfica, límites difusos, las reglas, el caso obligatorio y ponderación por confianza.
