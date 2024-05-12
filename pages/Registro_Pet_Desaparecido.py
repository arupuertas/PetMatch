import streamlit as st

def load_reports():
    if 'reports' not in st.session_state:
        st.session_state.reports = []
    return st.session_state.reports

def main():
    # Título do aplicativo
    st.title("Relatório de Animais Desaparecidos")
    
    # Menu de abertura
    menu_options = ["Registrar Novo Relatório", "Ver Relatórios Anteriores"]
    choice = st.sidebar.selectbox("Escolha uma opção:", menu_options)
    
    reports = load_reports()

    if choice == "Registrar Novo Relatório":
        report_animal(reports)
    elif choice == "Ver Relatórios Anteriores":
        view_reports(reports)

def report_animal(reports):
    # Formulário para inserir informações sobre o animal desaparecido
    with st.form("report_form"):
        st.header("Informe sobre o Animal Desaparecido")
        
        animal_type = st.selectbox("Tipo de Animal:", ["Cachorro", "Gato", "Outro"])
        breed = st.text_input("Raça:")
        color = st.text_input("Cor:")
        location = st.text_input("Localização (Cidade, Estado):")
        description = st.text_area("Descrição:")
        photo = st.file_uploader("Faça o upload de uma foto do animal (opcional):", type=["jpg", "jpeg", "png"])
        
        submit_button = st.form_submit_button("Enviar Relatório")

    # Se o formulário for enviado, processar os dados
    if submit_button:
        # Salvar os dados na lista de relatórios
        new_report = {
            "Tipo de Animal": animal_type,
            "Raça": breed,
            "Cor": color,
            "Localização": location,
            "Descrição": description,
            "Foto": photo
        }
        reports.append(new_report)
        
        # Exibir mensagem de sucesso
        st.success("O relatório foi enviado com sucesso!")

def view_reports(reports):
    # Exibir relatórios anteriores
    st.header("Relatórios Anteriores")
    for i, report in enumerate(reports):
        st.subheader(f"Relatório #{i + 1}")
        st.write(f"Tipo de Animal: {report['Tipo de Animal']}")
        st.write(f"Raça: {report['Raça']}")
        st.write(f"Cor: {report['Cor']}")
        st.write(f"Localização: {report['Localização']}")
        st.write(f"Descrição: {report['Descrição']}")
        if report['Foto'] is not None:
            st.image(report['Foto'], caption="Foto do Animal Desaparecido", use_column_width=True)
        else:
            st.write("Nenhuma foto fornecida.")

if __name__ == "__main__":
    main()
