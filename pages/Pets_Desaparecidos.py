import streamlit as st

def main():
    # Título do aplicativo
    st.title("Fotos de Animais Desaparecidos")

    # Exibir fotos de animais desaparecidos
    show_missing_animals()

def show_missing_animals():
    # Título da seção
    st.header("Animais Desaparecidos")

    # Lista de URLs das fotos de animais desaparecidos (substitua com suas próprias URLs)
    animal_photos = [
        "https://example.com/animal1.jpg",
        "https://example.com/animal2.jpg",
        "https://example.com/animal3.jpg"
    ]

    # Exibir cada foto em uma linha
    for photo_url in animal_photos:
        st.image(photo_url, caption="Animal Desaparecido", use_column_width=True)

if __name__ == "__main__":
    main()
