import streamlit as st

def main():
    # Título do aplicativo
    st.title("Aplicativo de Relatório de Animais Desaparecidos")

def show_home_page():
    st.write("""
    # Bem-vindo ao Aplicativo de Relatório de Animais Desaparecidos!

    Este aplicativo permite que você registre novos relatórios de animais desaparecidos ou visualize relatórios anteriormente registrados. 
    Use o menu à esquerda para navegar nas opções disponíveis.
    """)


if __name__ == "__main__":
    main()
