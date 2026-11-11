import argparse
from .config import ConfiguracionAG
from .genetico import ejecutar
from .estrella import sumas_lineas
from .visualizacion import graficar

def main():
    parser = argparse.ArgumentParser(description="Resuelve la estrella mágica mediante un algoritmo genético.")
    parser.add_argument("--poblacion", type=int, default=100); parser.add_argument("--generaciones", type=int, default=1000)
    parser.add_argument("--mutacion", type=float, default=.15); parser.add_argument("--elitismo", type=int, default=2)
    parser.add_argument("--torneo", type=int, default=3); parser.add_argument("--semilla", type=int, default=42)
    parser.add_argument("--salida", default="resultados/estrella.png"); args = parser.parse_args()
    resultado = ejecutar(ConfiguracionAG(args.poblacion, args.generaciones, args.mutacion, args.elitismo, args.torneo, args.semilla))
    print(f"Encontrada: {resultado.encontrado} | generación: {resultado.generaciones} | fitness: {resultado.mejor_fitness}")
    print(f"Individuo: {resultado.mejor_individuo}\nSumas: {sumas_lineas(resultado.mejor_individuo)}")
    print(f"Gráfica: {graficar(resultado.mejor_individuo, args.salida)}")

if __name__ == "__main__": main()
