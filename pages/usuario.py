import streamlit as st
import time
from components.nova_ideia import criar_nova_ideia
from components.minhas_ideias import listar_ideias

st.set_page_config(layout="wide", page_title="Aba de admin")

if "usuario" not in st.session_state:
    st.error("Você precisa estar logado para acessar essa página.")
    time.sleep(2)
    st.switch_page("pages/login.py")
    
    
with st.container():    
    st.title("Sistema de Ideias Intermetro")
abas = st.tabs(["Nova ideia", "Minhas ideias"])

with abas[0]:
    
    criar_nova_ideia()
with abas[1]:
    
    listar_ideias()
