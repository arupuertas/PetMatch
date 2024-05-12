import streamlit as st
import folium
from streamlit_folium import folium_static

def main():
    st.set_page_config(page_title="Mapa", page_icon='🐈‍⬛')
    logo = 'src/img/logo.png'
    st.image(logo, width=220, use_column_width=False)
    st.title("Mapa de Pets Desaparecidos em Sorocaba")
    show_missing_pets_map()

def show_missing_pets_map():
    sorocaba_center = (-23.5015, -47.4521)
    map_sorocaba = folium.Map(location=sorocaba_center, zoom_start=12)

    missing_pets_locations = [
        {"location": (-23.501326564994017, -47.426829469878804), "pet_photo": "src/img/1.png", "neighborhood": "Parque Três Meninos"},
        {"location": (-23.487277497754214, -47.465307000302175), "pet_photo": "src/img/2.png", "neighborhood": "Vila Carvalho"},
        {"location": (-23.471289211943557, -47.44671036852105), "pet_photo": "src/img/3.png", "neighborhood": "Parque das Águas"},
        {"location": (-23.49991452871889, -47.45490781634348), "pet_photo": "src/img/4.png", "neighborhood": "Centro"},
        {"location": (-23.50611721343325, -47.43492744045656), "pet_photo": "src/img/5.png", "neighborhood": "Vila Haro"},
        {"location": (-23.522354082411706, -47.4627605477133), "pet_photo": "src/img/6.png", "neighborhood": "Campolim"},
        {"location": (-23.537153555389796, -47.45114569673409), "pet_photo": "src/img/7.png", "neighborhood": "Centro Votorantim"},
        {"location": (-23.538622874928702, -47.492664708696424), "pet_photo": "src/img/8.png", "neighborhood": "Jardim Tatiana"},

    ]

    # Mapeando localizações para fotos e bairros
    pet_photos = {info["neighborhood"]: info["pet_photo"] for info in missing_pets_locations}

    for location in missing_pets_locations:
        folium.Marker(
            location=location["location"],
            popup=f"Pet Desaparecido em {location['neighborhood']}!",
            icon=folium.Icon(color='red')
        ).add_to(map_sorocaba)

    folium_static(map_sorocaba)

    # Selecionando o bairro do pet desaparecido
    selected_neighborhood = st.selectbox(
        "Selecione o bairro do Pet Desaparecido:",
        [location["neighborhood"] for location in missing_pets_locations]
    )
    
    if selected_neighborhood:
        pet_photo = pet_photos[selected_neighborhood]
        st.image(pet_photo, width=300)

if __name__ == "__main__":
    main()