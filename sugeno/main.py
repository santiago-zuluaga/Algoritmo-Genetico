import argparse
from .motor_sugeno import evaluar
from .incertidumbre import evaluar_con_confianza

def imprimir(titulo, r):
    print(f"\n{titulo}\nPertenencias: {r.grados}\nActivación/peso: {r.activaciones}\nConsecuentes: {r.consecuentes}")
    print(f"Salida ponderada: {r.salida} | Clase: {r.clasificacion}")

def main():
    p = argparse.ArgumentParser(description="Clasificador Iris Sugeno de orden cero.")
    p.add_argument("--petalwidth", type=float, default=1.6); p.add_argument("--petallength", type=float, default=5.0)
    a = p.parse_args(); imprimir("Sugeno convencional", evaluar(a.petalwidth, a.petallength))
    imprimir("Sugeno ponderado por confianza", evaluar_con_confianza(a.petalwidth, a.petallength))

if __name__ == "__main__": main()
