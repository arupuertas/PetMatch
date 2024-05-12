import streamlit as st

def main():
    st.set_page_config(page_title="Grupo UPX", page_icon='🐈‍⬛')
    logo = 'src/img/logo.png'
    st.image(logo, width=220, use_column_width=False)
    st.title("Página de Apresentação")

    st.write("""
    ## GRUPO UPX V:

    ### Aruã Puertas Costa
    E-mail: aruapc@hotmail.com  
    RA: 132588

    ### Roberto Elias de Souza
    E-mail: robertoeliassouza@gmail.com  
    RA: 223657

    ### Silvio de Campos Junior
    E-mail: scjunior95@gmail.com   
    RA: 132277

    ## Sobre o Projeto:

    Facilitar a adoção de animais e o report de animais desaparecidos.

    """)

if __name__ == "__main__":
    main()
