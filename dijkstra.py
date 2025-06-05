import heapq

def dijkstra(grafo, inicio):
    distancia = {v: float('inf') for v in grafo}
    distancia[inicio] = 0
    fila = [(0, inicio)]
    anterior = {v: None for v in grafo}

    while fila:
        dist_atual, vertice_atual = heapq.heappop(fila)

        for vizinho, peso in grafo[vertice_atual].items():
            dist = dist_atual + peso
            if dist < distancia[vizinho]:
                distancia[vizinho] = dist
                anterior[vizinho] = vertice_atual
                heapq.heappush(fila, (dist, vizinho))

    return distancia, anterior

def reconstruir_caminho(anterior, destino):
    caminho = []
    atual = destino
    while atual:
        caminho.insert(0, atual)
        atual = anterior[atual]
    return caminho

