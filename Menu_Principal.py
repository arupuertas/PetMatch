import streamlit as st

def main():
    #GRUPO:
    
    #Aruã Puertas Costa
    #RA: 132588

    #Roberto Elias de Souza
    #RA: 223657
    
    #Silvio de Campos Junior 
    #RA: 132277
    
    st.set_page_config(page_title="PET Match", page_icon='🐈‍⬛')
    logo = 'src/img/logo.png'
    st.image(logo, width=220, use_column_width=False)
    st.title("PetMatch")
    st.subheader('O SEU :blue[APP] PET', divider='rainbow')
    st.subheader('Acesse o menu lateral e use nossos serviços de adoção e report de animais perdidos.')

if __name__ == "__main__":
    main()
