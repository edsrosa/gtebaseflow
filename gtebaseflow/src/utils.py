import pandas as pd
import streamlit as st


def start_session_states():
    """Inicializa o sesseion state"""
    states = {'files_byname_q': {}}
    for k,v in states.items():
        if k not in st.session_state:
            st.session_state[k] = v


def select_inline(lb, ops, key_id, index=0,  pc=0.5):
    """Gera entrada para selecionar nome de coluna."""
    c01, c02 = st.columns([pc, 1-pc])
    c01.write(lb)
    select_in = c02.selectbox(lb, options=ops, key=key_id, index=index, label_visibility='collapsed')
    return select_in


def get_files_byname(files_up):
    """Recupera as propriedades do arquivo carregados."""
    files_byname  = {}
    if files_up != []:
        for f in files_up:
            files_byname[f.name] = f
        
    return files_byname


def get_filename(files_byname):
    """Recupera o nome do arquivo atual."""
    if files_byname != {}:
        filename = select_inline(lb="Arquivo: ", ops=files_byname.keys(), key_id='filename', index=0,  pc=0.5)
    else:
        filename = None
    
    return filename


def get_shtname(filename, files_byname):
    """Recupera o nome da aba atual."""
    if filename is not None and files_byname != {}:
        file = files_byname[filename]
        shtnames = list(pd.ExcelFile(file).sheet_names)
        shtname = select_inline(lb="Planilha:", ops=shtnames, key_id='sht_name')
    else:
        shtname = None
    
    return shtname


def get_colsname(files_byname, filename, sht_name):
    """Recupera o nome das colunas do arquivo atual."""
    cols_name = []
    if sht_name is not None:
        df = pd.read_excel(files_byname[filename], sheet_name=sht_name)
        cols_name = list(df.columns)

    return cols_name


def load_xlsx(title, label_up, multiple):
    """Expander com carregamento de arquivos xlsx."""
    with st.expander(title, expanded=True):
        files_up = st.file_uploader(label_up, 
                                    type='xlsx',  accept_multiple_files=multiple, 
                                    )
        
        files_byname = get_files_byname(files_up)
        filename = get_filename(files_byname)
        shtname = get_shtname(filename, files_byname)
        cols_name = get_colsname(files_byname, filename, shtname)

        col_datetime = select_inline(lb='Data:', ops=cols_name, index=None, key_id='col_datetime_q')
        col_streamflow = select_inline(lb='Vazão (m³/s):', ops=cols_name, index=None, key_id='col_streamflow_q')

        return files_up, files_byname, filename, shtname, cols_name, col_datetime, col_streamflow 
        