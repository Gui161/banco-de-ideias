import streamlit as st
from data.crud import listar_ideias_por_usuario

def listar_ideias():
    with st.container(border=True):
        usuario = st.session_state['usuario']
        
        resultado = listar_ideias_por_usuario(usuario_id= usuario['id'])
        if resultado['status'] == "sucesso":
            ideias = resultado['retorno']
            colunas = st.columns(3)
            for i, ideia in enumerate(ideias):
                with colunas[i]:
                    with st.container(border=True):
                        st.markdown(f"### {ideia.titulo}", text_alignment="center")
                        st.write(f"Status: {ideia.status}")
                
        else:
            st.error(resultado['retorno'])
