import streamlit as st

paginas = st.navigation([
    st.Page("./pages/login.py", title="Login"),
    st.Page("./pages/admin.py", title="Central Admin"),
    
    
], position="hidden")

paginas.run()

