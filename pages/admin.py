import streamlit as st
from components.nova_ideia import criar_nova_ideia
import time


st.set_page_config(layout="wide", page_title="Aba de admin")

if "usuario" not in st.session_state:
    st.error("Você precisa estar logado para acessar essa página.")
    time.sleep(2)
    st.switch_page("pages/login.py")
    

st.title("Tela de admin")
abas = st.tabs(["Nova Ideia", "Minhas ideias", ])

with abas[0]:
    criar_nova_ideia()

with abas[1]:
    st.text("teste2")
    