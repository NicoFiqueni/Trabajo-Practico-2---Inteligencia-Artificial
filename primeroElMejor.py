# Nombre: Nicolas Fiqueni
# Legajo: INF388-11805

import heapq

def leer_relieve(actual, meta):
    # simulamos el sensor leyendo la distancia que falta para llegar
    return abs(actual - meta)

def primero_el_mejor(inicio_B, meta_A, paso, limite=10):
    cola_prioridad = []
    # aca guardamos la distancia estimada y la posicion
    heapq.heappush(cola_prioridad, (leer_relieve(inicio_B, meta_A), inicio_B))
    visitados = set([inicio_B])
    movimientos = 0

    print("\nArrancando Primero el Mejor")

    while cola_prioridad:
        h, actual = heapq.heappop(cola_prioridad)
        movimientos += 1
        print(f"Revisando posicion: {actual} (Falta aprox: {h})")

        if actual == meta_A:
            print(f"Listo! Punto encontrado en {movimientos} movimientos.")
            return actual

        sucesores = [actual + paso, actual - paso]

        for suc in sucesores:
            # solo las posiciones no revisadas y dentro del recorrido permitido
            if abs(suc - inicio_B) <= limite and suc not in visitados:
                visitados.add(suc)
                # calculamos cuanto falta desde la nueva posicion
                faltante = leer_relieve(suc, meta_A)
                heapq.heappush(cola_prioridad, (faltante, suc))

    print("No se encontro el punto dentro del recorrido permitido: "
          "hay que llamar al tecnico.")
    return None

# realizamos la prueba
primero_el_mejor(0, 3, 1)
