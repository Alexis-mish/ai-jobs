""""
Alumno: Alexis Michell Hernandez Robledo
Universidad Politecnica del Estado de Nayarit
I-SOFT8
Problema:
Write a Python program that, given two jugs of 50 L and 30 L capacity and a user-supplied target volume, prints the shortest sequence of moves to reach that exact volume in either jug—or reports that the target is impossible.
"""
from collections import deque #Usamos esto para tener una lista especial llamada deque (como una fila de personas en el súper). Nos ayuda a guardar todos los estados que vamos probando.

def resolver(cap1, cap2, objetivo): #Esta función intenta encontrar la forma más corta de llegar al número que se pide
    visitados = set() #visitados es una lista donde vamos guardando lugares donde ya hemos estado (combinaciones de litros).
    cola = deque() #es como una lista de cosas por intentar.

    # Estado inicial: (jarra1, jarra2, lista de pasos)
    cola.append((0, 0, [])) # Al inicio ambas jarras estan vacias

    while cola:
        j1, j2, pasos = cola.popleft() #Sacamos el primer estado de la cola.

        if (j1, j2) in visitados: #j1 es jarra1 (50l) y j2 es jarra2 (30l)
            continue
        visitados.add((j1, j2)) #Guardamos el estado en la lista de visitados.

        if j1 == objetivo or j2 == objetivo: #Si llegamos al objetivo, imprimimos la secuencia de pasos y terminamos
            return pasos + [("Meta alcanzada", j1, j2)]

        # Posibles movimientos
        movimientos = [ 
            ("Llenar jarra1", cap1, j2),
            ("Llenar jarra2", j1, cap2),
            ("Vaciar jarra1", 0, j2),
            ("Vaciar jarra2", j1, 0),
            ("Verter jarra1 → jarra2", max(0, j1 - (cap2 - j2)), min(cap2, j2 + j1)),
            ("Verter jarra2 → jarra1", min(cap1, j1 + j2), max(0, j2 - (cap1 - j1))),
        ]

        for accion, nuevo_j1, nuevo_j2 in movimientos: #Probamos cada movimiento, y si aún no lo hemos probado antes, lo agregamos a la fila.
            nuevo_pasos = pasos + [(accion, nuevo_j1, nuevo_j2)]
            cola.append((nuevo_j1, nuevo_j2, nuevo_pasos))

    return None  # No se puede lograr

def main(): #Esta función es la que se ejecuta al principio, y es la que llama a resolver.
    cap1 = 50 
    cap2 = 30

    try: 
        objetivo = int(input("Ingresa el volumen objetivo (10 a 50 L, múltiplo de 10): "))
        if objetivo <= 0 or objetivo > cap1 or objetivo % 10 != 0: 
            raise ValueError
    except ValueError: 
        print("Entrada no válida. Debe ser un número entre 10 y 50, múltiplo de 10.")
        return

    resultado = resolver(cap1, cap2, objetivo)

    print(f" Objetivo: {objetivo} litros")

    if resultado: #Si el resultado no es None, significa que encontramos una forma de llegar al objetivo.
        for i, (accion, j1, j2) in enumerate(resultado): #Imprimimos cada paso de la secuencia de pasos.
            print(f"Paso {i + 1}: {accion:22} → (jarra1: {j1} L, jarra2: {j2} L)") 
        print(f"Total de pasos: {len(resultado)}") 
    else:
        print(f"No se puede obtener exactamente {objetivo} litros con estas jarras.")

if __name__ == "__main__":
    main()
