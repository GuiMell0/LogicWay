import folium
import openrouteservice

def gerar_mapa(rota, coordenadas, destino_usuario, nome_arquivo='rota_hospital.html'):
    client = openrouteservice.Client(key='5b3ce3597851110001cf624889bff0f4ebdc420f87ea046ccb5477ba')

    pontos_coord = [[coordenadas[local][1], coordenadas[local][0]] for local in rota]
    rota_api = client.directions(coordinates=pontos_coord, profile='driving-car', format='geojson')

    props = rota_api['features'][0]['properties']['segments'][0]
    dist_km = round(props['distance'] / 1000, 2)

    print(f"Distância: {dist_km} km")

    mapa = folium.Map(location=coordenadas["Hospital Municipal Dr. Ernesto Che Guevara"], zoom_start=11)
    folium.GeoJson(rota_api, name="Rota").add_to(mapa)

    for local in rota:
        folium.Marker(
            location=coordenadas[local],
            tooltip=local,
            icon=folium.Icon(color="green" if local == destino_usuario else "blue")
        ).add_to(mapa)

    mapa.save(nome_arquivo)
    print(f"\nMapa salvo no arquivo '{nome_arquivo}'")

