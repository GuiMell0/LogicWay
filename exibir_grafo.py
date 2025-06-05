import networkx as nx
import matplotlib.pyplot as plt

def mostrar_grafo(grafo, rota, destino_usuario):
    G = nx.Graph()
    for origem in grafo:
        for destino in grafo[origem]:
            peso = grafo[origem][destino]
            G.add_edge(origem, destino, weight=peso)

    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(12, 8))
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color='lightblue')
    nx.draw_networkx_edges(G, pos, width=1)
    nx.draw_networkx_labels(G, pos, font_size=9, font_weight='bold')

    path_edges = list(zip(rota, rota[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=3, edge_color='red')

    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=8)

    plt.title(f"Melhor caminho até {destino_usuario}")
    plt.axis('off')
    plt.show()

