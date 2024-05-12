import streamlit as st

def main():
    # Título do aplicativo
    st.title("Página de Apresentação")

    # Conteúdo da página de apresentação
    st.write("""
    # Bem-vindo à nossa página de apresentação do projeto!

    Este aplicativo foi desenvolvido por uma equipe dedicada. Abaixo, você encontrará informações sobre os membros da equipe e seus papéis no projeto.

    ## Equipe

    ### João Silva
    Desenvolvedor Full Stack

    ### Maria Santos
    Designer de UX/UI

    ### Pedro Oliveira
    Especialista em Negócios

    ### Ana Rodrigues
    Gerente de Projeto

    ### Laura Costa
    Especialista em Marketing

    ## Sobre o Projeto

    Este projeto tem como objetivo ajudar a reunir pets desaparecidos com seus donos. Se você encontrar um pet perdido, por favor, entre em contato conosco para que possamos ajudar a reunir a família novamente!

    """)

if __name__ == "__main__":
    main()
