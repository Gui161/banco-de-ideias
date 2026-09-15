import streamlit as st


st.title("Banco de Idéias Intermetro")

if "usuario" not in st.session_state:
    with st.form("login"):
        email = st.text_input(label="Email", type='email')
        senha = st.text_input(label="Senha", type="password" )
        login_btn = st.form_submit_button(label="Login", width='stretch')