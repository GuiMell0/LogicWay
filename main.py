from grafos import grafo, coordenadas
from dijkstra import dijkstra, reconstruir_caminho
from exibir_grafo import mostrar_grafo
from exibir_mapa import gerar_mapa

def main():
    print("Hospitais disponíveis:")
    locais = list(coordenadas.keys())
    
    origem = "Hospital Municipal Dr. Ernesto Che Guevara"
    destinos = [nome for nome in locais if nome != origem]
    
    for i, nome in enumerate(destinos, 1):
        print(f"{i}. {nome}")

    opcao = int(input("Escolha o número do hospital destino: "))
    destino_usuario = destinos[opcao - 1]

    distancia, anteriores = dijkstra(grafo, origem)
    rota = reconstruir_caminho(anteriores, destino_usuario)

    print(f"\n Melhor caminho até {destino_usuario}:")
    print(" -> ".join(rota))

    gerar_mapa(rota, coordenadas, destino_usuario)
    mostrar_grafo(grafo, rota, destino_usuario)

if __name__ == "__main__":
    main()
