import streamlit as st
from streamlit_folium import folium_static
import folium

def main():
    # Título do aplicativo
    st.title("Mapa de Pets Desaparecidos em Sorocaba")

    # Exibir o mapa de Sorocaba com marcadores de pets desaparecidos
    show_missing_pets_map()

def show_missing_pets_map():
    # Coordenadas do centro de Sorocaba
    sorocaba_center = (-23.5015, -47.4521)

    # Criar o mapa de Sorocaba
    map_sorocaba = folium.Map(location=sorocaba_center, zoom_start=12)

    # Adicionar marcadores de pets desaparecidos (exemplo com coordenadas aleatórias)
    missing_pets_locations = [
        (-23.4965, -47.4573),
        (-23.5010, -47.4402),
        (-23.5055, -47.4650)
    ]

    for location in missing_pets_locations:
        folium.Marker(location=location, popup="Pet Desaparecido").add_to(map_sorocaba)

    # Renderizar o mapa
    folium_static(map_sorocaba)

if __name__ == "__main__":
    main()
