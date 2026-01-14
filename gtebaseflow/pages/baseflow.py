import streamlit as st

def select_box(label, options):
    """Select box com rótulo ao lado da baixa e não acima."""
    row = st.container()
    col01, col02 = row.columns(2)
    rotulo = col01.write(label)
    select = col02.selectbox("label" + "_select", options=options)
    return select


def controls():
    """Controles para inserção dos dados e análises."""
    with st.sidebar.expander("Arquivos de Entrada"):
        files_up = st.file_uploader(label="Inserir Arquivos:", type=["xlsx"], accept_multiple_files=True, width="stretch")

    
    with st.sidebar.expander("Plotagem"):
        fl = st.selectbox("Arquivo", options=['f01', 'f02'])

            
    with st.sidebar.expander("Separação Escoamento de Base"):
        k_value = st.number_input(label="K:", value=100)


    with st.sidebar.expander("Exportar Resultados"):
        st.button("Baixar dados", use_container_width=True)


def content():
    """Conteúdo da página."""
    
    st.sidebar.markdown("""## Separador de Fluxo de Base""")
    controls()

baseflow = st.Page(content, 
               title="Separador de Fluxo de Base",
               icon=":material/hexagon:",
               )
