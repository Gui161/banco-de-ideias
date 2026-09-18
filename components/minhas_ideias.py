import streamlit as st
from data.crud import listar_ideias_por_usuario

def listar_ideias():
    with st.container(border=True):
        usuario = st.session_state['usuario']
        
        resultado = listar_ideias_por_usuario(usuario_id= usuario['id'])
        if resultado['status'] == "sucesso":
            ideias = resultado['retorno']
            for i in range(0, len(ideias), 3):
                colunas = st.columns(3)
                for j, ideia in enumerate(ideias[i:i+3]):
                    with colunas[j]:
                        with st.container(border=True):
                            st.markdown(f"### {ideia.titulo}")
                            st.write(f"Status {ideia.status}")
                
        else:
            st.error(resultado['retorno'])
