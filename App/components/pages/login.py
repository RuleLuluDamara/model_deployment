import streamlit as st


def show():
    """Render the login page"""
    st.title("Login")
    st.markdown("Silakan masuk dengan akun Anda")

    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        remember_me = st.checkbox("Remember me")
        submitted = st.form_submit_button("Login")

        if submitted:
            if username == "admin" and password == "password":
                st.success("Login berhasil!")
            else:
                st.error("Username atau password salah")
