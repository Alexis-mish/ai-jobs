""""
Alumno: Alexis Michell Hernandez Robledo
Universidad Politecnica del Estado de Nayarit
I-SOFT8
Problema:
Write a Python program that, given two jugs of 50 L and 30 L capacity and a user-supplied target volume, prints the shortest sequence of moves to reach that exact volume in either jug—or reports that the target is impossible.
"""

class Estado:
    def __init__(self, jarra1, jarra2, pasos=None, accion="Inicio"):
        self.jarra1 = jarra1
        self.jarra2 = jarra2
        self.pasos = pasos or []
        self.accion = accion


def main():
    # Se pide el objetivo el objetivo en litros
    try:
        objetivo = int(input("Ingrese el objetivo en litros: "))
    except ValueError:
        print("Error: El objetivo debe ser un número entero")

if __name__ == "__main__":
    pass