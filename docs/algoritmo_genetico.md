# Algoritmo genético: estrella mágica

El cromosoma es una permutación de 1 a 12, donde cada índice representa A–L. Las seis líneas se guardan como índices en `estrella.py`. La función objetivo es \(F(x)=\sum_{i=1}^{6}|S_i(x)-26|\); por ello, F=0 equivale a cumplir las seis restricciones simultáneamente.

La población inicial se genera mezclando aleatoriamente los doce valores. La selección por torneo toma una muestra y escoge el menor fitness. OX copia un segmento de un padre y completa los huecos según el orden circular del otro, preservando la permutación. La mutación intercambia dos posiciones con la probabilidad configurada. El elitismo copia los mejores sin alterarlos.

La semilla alimenta un generador local y permite repetir una corrida. No hay garantía de encontrar solución en un presupuesto finito; el resultado siempre informa el mejor cromosoma observado. La figura coloca las doce posiciones conectadas por las seis líneas y etiqueta sus sumas.
