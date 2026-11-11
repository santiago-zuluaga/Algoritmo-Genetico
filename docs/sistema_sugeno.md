# Sistema Sugeno para Iris

El sistema Sugeno de orden cero representa setosa, versicolor y virginica mediante 0, 1 y 2. Las funciones trapezoidales de `ConjuntosIris` suavizan los límites lingüísticos: los hombros y rampas solapan las categorías alrededor de 0.6/1.5 cm de ancho y 2.0/4.9 cm de largo. Los extremos de soporte y mesetas se exponen como parámetros. Se mantienen los umbrales del árbol, incluyendo 1.7; no se reemplazan por 1.5.

Las condiciones numéricas de cada regla se difuminan mediante rampas lineales de ancho 0.2 centradas en cada frontera. Las conjunciones usan mínimo. El consecuente de cada regla es una constante y la salida es \(z=\sum w_i z_i/\sum w_i\). Si todos los pesos son cero, salida y clase son `None`. La clase final es el consecuente numérico más cercano (empate hacia la clase con menor índice).

El modo de incertidumbre multiplica cada activación por la confianza observada en la hoja asociada: correctos/(correctos+incorrectos). Es un promedio Sugeno reponderado, no un modelo estadístico de calibración. Para 1.6 y 5.0 hay solapamiento de las reglas fronterizas R3–R5 y el promedio continuo se cuantiza con la política descrita; el programa imprime todos los pesos y el resultado para que la decisión sea auditable.
