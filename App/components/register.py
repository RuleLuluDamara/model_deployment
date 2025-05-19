import streamlit as st
import time
from components.auth import users_db, hash_password


def register_page():
    """Beautiful registration page"""
    with st.container():
        st.markdown("""
        <div class="form-container animated">
            <h1 class="form-title">Create Account</h1>
        """, unsafe_allow_html=True)

        with st.form("register_form"):
            name = st.text_input("Full Name", key="register_name")
            email = st.text_input("Email Address", key="register_email")
            password = st.text_input(
                "Password", type="password", key="register_password")
            confirm_password = st.text_input(
                "Confirm Password", type="password", key="register_confirm_password")

            if st.form_submit_button("Sign Up", type="primary"):
                with st.spinner("Creating account..."):
                    time.sleep(1)
                    if not name or not email or not password or not confirm_password:
                        st.error("Please fill in all fields")
                    elif password != confirm_password:
                        st.error("Passwords do not match")
                    elif email in users_db:
                        st.error("Email already registered")
                    else:
                        users_db[email] = {
                            "name": name,
                            "password": hash_password(password)
                        }
                        st.session_state.user = {
                            "email": email,
                            "name": name
                        }
                        st.success("Registration successful!")
                        time.sleep(1)
                        st.query_params["page"] = "predict"
                        st.rerun()

        st.markdown("""
            <div style="text-align: center; margin-top: 25px;">
                <p style="color: #666;">Already have an account? <a href="?page=login" style="color: var(--primary); font-weight: 500
                ;">Login</a></p>
            </div>
        </div>
        """, unsafe_allow_html=True)
