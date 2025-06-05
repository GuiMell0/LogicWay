import random
from grafos import grafo, coordenadas
from dijkstra import dijkstra, reconstruir_caminho
from exibir_grafo import mostrar_grafo
from exibir_mapa import gerar_mapa


def gerar_condicoes(): 
    clima = random.random() < 0.25   
    transito = random.random() < 0.2      
    acidentes = random.random() < 0.15    
    obras = random.random() < 0.05     
    return clima, transito, acidentes, obras


def aplicar_condicoes(grafo_original, clima, transito, acidentes, obras):
    grafo_atualizado = {}

    for origem in grafo_original:
        grafo_atualizado[origem] = {}
        for destino, tempo in grafo_original[origem].items():
            tempo_atualizado = tempo
            if clima:
                tempo_atualizado += 15
            if transito:
                tempo_atualizado += 20
            if acidentes:
                tempo_atualizado += 10
            if obras:
                tempo_atualizado += 5
            grafo_atualizado[origem][destino] = tempo_atualizado

    return grafo_atualizado


def main():
    print("\nSistema de Rotas para Transporte de Órgãos")

    clima, transito, acidentes, obras = gerar_condicoes()

    print("\nCondições atuais detectadas automaticamente:")
    if not any([clima, transito, acidentes, obras]):
        print("Condições normais, sem interferências nas rotas.")
    else:
        if clima:
            print("Clima: Chuvoso (+15 min)")
        if transito:
            print("Trânsito: Pesado (+20 min)")
        if acidentes:
            print("Acidentes: Presentes (+10 min)")
        if obras:
            print("Obras: Presentes (+5 min)")

    print("\nHospitais disponíveis para destino:")
    locais = list(coordenadas.keys())

    origem = "Hospital Municipal Dr. Ernesto Che Guevara"
    destinos = [nome for nome in locais if nome != origem]

    for i, nome in enumerate(destinos, 1):
        print(f"{i}. {nome}")

    opcao = int(input("Escolha o número do hospital destino: "))
    destino_usuario = destinos[opcao - 1]


    grafo_atualizado = aplicar_condicoes(grafo, clima, transito, acidentes, obras)

    distancia, anteriores = dijkstra(grafo_atualizado, origem)
    rota = reconstruir_caminho(anteriores, destino_usuario)

    print(f"\nMelhor caminho até {destino_usuario}:")
    print(" -> ".join(rota))
    print(f"\nTempo estimado: {distancia[destino_usuario]} minutos")

    gerar_mapa(rota, coordenadas, destino_usuario)
    mostrar_grafo(grafo_atualizado, rota, destino_usuario)

if __name__ == "__main__":
    main()