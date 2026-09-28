# Nombre: Nicolas Fiqueni
# Legajo: INF388-11805

from collections import deque

def busqueda_anchura(inicio_B, meta_A, paso, limite=10):
    # aca usamos una cola FIFO para ir guardando los lugares a revisar
    cola = deque([inicio_B])
    visitados = set([inicio_B])
    movimientos = 0

    print("Arrancando busqueda en anchura")

    while cola:
        actual = cola.popleft()
        movimientos += 1
        print(f"Revisando posicion: {actual}")

        # aca simulamos que el robot palpo y encontro el punto A
        if actual == meta_A:
            print(f"Listo! Punto encontrado en {movimientos} movimientos.")
            return actual

        # vemos los siguientes pasos (derecha e izquierda)
        derecha = actual + paso
        izquierda = actual - paso

        # agregamos a la cola si no los revisamos antes
        # y si estan dentro del recorrido permitido
        if abs(derecha - inicio_B) <= limite and derecha not in visitados:
            visitados.add(derecha)
            cola.append(derecha)

        if abs(izquierda - inicio_B) <= limite and izquierda not in visitados:
            visitados.add(izquierda)
            cola.append(izquierda)

    print("No se encontro el punto dentro del recorrido permitido: "
          "hay que llamar al tecnico.")
    return None

# realizamos la prueba
busqueda_anchura(0, 3, 1)
