import streamlit as st
import random
import time 

def load_images():
    return [
        "src/img/01.png",
        "src/img/02.png",
        "src/img/03.png",
        "src/img/04.png",
        "src/img/05.png",
    ]

def display_pet(image):
    st.image(image, width=300, use_column_width=True)  

def swipe_buttons(image):
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        left_button, right_button = st.columns(2) 
        if left_button.button("Próximo Pet"):
            st.session_state['swiped_left'] += 1
            st.warning("Procurando outro pet...")
            time.sleep(1)  # Pausa antes de recarregar
            move_to_next_pet()

        if right_button.button("Pet Match"):
            st.session_state['swiped_right'] += 1
            st.session_state['matches'].append(image)
            st.success("Deu match! 💖")
            time.sleep(1)  # Pausa antes de recarregar
            move_to_next_pet()

def move_to_next_pet():
    images = load_images()
    st.session_state['current_image'] = random.choice(images)
    st.rerun()  # Recarrega a página para mudar a imagem

def setup_page():
    st.set_page_config(page_title="PetMatch", page_icon='🐈‍⬛')
    st.image('src/img/logo.png', width=220, use_column_width=False)
    st.title("Dê ❤️ Match com seu próximo Pet")
    st.write("""
        ## Bem vindo ao sistema de adoção PetMatch!
        Arraste para a direita para dar Match ou arraste para a esquerda para continuar procurando.
    """)

def display_matches():
    if st.session_state['matches']:
        st.write("## Seus Matches:")
        cols = st.columns(len(st.session_state['matches']))
        for idx, img in enumerate(st.session_state['matches']):
            cols[idx].image(img, width=100)

def main():
    setup_page()
    
    if 'swiped_left' not in st.session_state:
        st.session_state['swiped_left'] = 0
    if 'swiped_right' not in st.session_state:
        st.session_state['swiped_right'] = 0
    if 'matches' not in st.session_state:
        st.session_state['matches'] = []
    if 'current_image' not in st.session_state:
        images = load_images()
        st.session_state['current_image'] = random.choice(images)

    display_pet(st.session_state['current_image'])
    swipe_buttons(st.session_state['current_image'])
    display_matches()

if __name__ == "__main__":
    main()