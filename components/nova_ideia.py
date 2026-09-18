import streamlit as st
from data.crud import salva_ideia

def criar_nova_ideia():
    usuario = st.session_state['usuario']
    
    with st.form("Formulario_criar_nova_ideia", clear_on_submit=True:
        st.title("Cadastro de novas Idéias", text_alignment="center")
        nome = st.text_input(label="Nome", value=usuario['nome'])
        setor = st.pills(label="Setor", options=["Comercial", "Logistica", "Laboratório", "P&D", "Qualidade", "Financeiro", "Manutenção", "Fabricação", "RH", "Compras", "Outros"], default="Laboratório")
        titulo_ideia = st.text_input(label="Titulo")
        problema = st.text_input("Problema identificado")
        beneficio = st.text_input("Beneficio esperado")
        categoria = st.text_input("Categoria da Inovação")
        area_impactada = st.text_input("Area Impactada.")
        solucao = st.text_area("Solução Proposta")
        cadastrar_ideia_btn = st.form_submit_button("Enviar", use_container_width=True, )
        if cadastrar_ideia_btn:
            conteudo = {"setor":setor, "problema":problema, "beneficio":beneficio, "categoria":categoria, "area_impactada":area_impactada, "solucao":solucao}
            resultado = salva_ideia(usuario['id'],titulo=titulo_ideia,conteudo= conteudo)
            if resultado['status'] == "sucesso":
                st.success(f"Ideia cadastrada com sucesso!")
                st.balloons()
                st.rerun()
                
            else:
                st.error(f"Erro ao cadatrar mensagem, {resultado['retorno']}")
            
            
        
        