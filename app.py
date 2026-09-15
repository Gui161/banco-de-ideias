import streamlit as st

paginas = st.navigation([
    st.Page("./pages/login.py", title="Login")
], position="hidden")

paginas.run()