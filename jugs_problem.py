""""
Alumno: Alexis Michell Hernandez Robledo
Universidad Politecnica del Estado de Nayarit
I-SOFT8
Problema:
Write a Python program that, given two jugs of 50 L and 30 L capacity and a user-supplied target volume, prints the shortest sequence of moves to reach that exact volume in either jug—or reports that the target is impossible.
"""

from collections import deque

class Estado:
    def __init__(self, jarra1, jarra2, pasos=None, accion="Inicio"):
        self.jarra1 = jarra1
        self.jarra2 = jarra2
        self.accion = accion
        self.pasos = pasos or []
    
    