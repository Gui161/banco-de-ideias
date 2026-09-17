import streamlit as st

def criar_nova_ideia():
    
    with st.form("Formulario_criar_nova_ideia"):
        st.title("Cadastro de novas Idéias", text_alignment="center")
        nome = st.text_input(label="Nome")
        setor = st.pills(label="Setor", options=["Comercial", "Logistica", "Laboratório", "P&D", "Qualidade", "Financeiro", "Manutenção", "Fabricação", "RH", "Compras", "Outros"], default="Laboratório")
        titulo_ideia = st.text_input(label="Titulo")
        problema = st.text_input("Problema identificado")
        beneficio = st.text_input("Beneficio esperado")
        categoria = st.text_input("Categoria da Inovação")
        area_impactada = st.text_input("Area Impactada.")
        solucao = st.text_area("Solução Proposta")
        cadastrar_ideia_btn = st.form_submit_button("Enviar", use_container_width=True)
        