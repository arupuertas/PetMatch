import streamlit as st
from streamlit_image_select import image_select

def main():
    st.set_page_config(page_title="Pets Desaparecidos", page_icon='🐈‍⬛')
    logo = 'src/img/logo.png'
    st.image(logo, width=220, use_column_width=False)
    st.title("Fotos de Animais Desaparecidos")

    show_missing_animals()

def show_missing_animals():
    st.header("Animais Desaparecidos")

    img = image_select("", ["src/img/1.png", "src/img/2.png", "src/img/3.png", "src/img/4.png", 
                                 "src/img/5.png", "src/img/6.png", "src/img/7.png", "src/img/8.png"])

    st.image((img))

if __name__ == "__main__":
    main()
