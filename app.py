import streamlit as st

paginas = st.navigation([
    st.Page("./pages/login.py", title="Login"),
    st.Page("./pages/admin.py", title="Central Admin"),
    st.Page("./pages/usuario.py", title="Central usuario"),
    
    
], position="hidden")

paginas.run()

