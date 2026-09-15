import streamlit as st
from data.crud import fazer_login


st.title("Banco de Idéias Intermetro", text_alignment="center")

if "usuario" not in st.session_state:
    with st.form("login"):
        email = st.text_input(label="Email", type='email')
        senha = st.text_input(label="Senha", type="password" )
        st.write("---")
        login_btn = st.form_submit_button(label="Login", width='stretch')
        
        if login_btn:
            if email == "" or senha == "":
                st.error("Preencha todos os campos para seguir")
            else:
                resultado = fazer_login(email=email, senha=senha)
                if resultado["status"] == "sucesso":
                    st.success(resultado['mensagem'])
                else:
                    st.error(resultado['mensagem'])
            
            