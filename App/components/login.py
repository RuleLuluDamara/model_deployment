import streamlit as st
import time
from components.auth import users_db, hash_password


def login_page():
    with st.container():
        st.markdown("""
        <div class="form-container animated">
            <h1 class="form-title">Welcome To NutrioMatic!</h1>
        """, unsafe_allow_html=True)

        with st.form("login_form"):
            email = st.text_input("Email Address", key="login_email")
            password = st.text_input(
                "Password", type="password", key="login_password")

            if st.form_submit_button("Login", type="primary"):
                with st.spinner("Authenticating..."):
                    time.sleep(1)
                    if not email or not password:
                        st.error("Please fill in all fields")
                    else:
                        hashed_password = hash_password(password)
                        if email in users_db and users_db[email]["password"] == hashed_password:
                            st.session_state.user = {
                                "email": email,
                                "name": users_db[email]["name"]
                            }
                            st.success("Login successful!")
                            time.sleep(0.5)
                            st.query_params["page"] = "predict"
                            st.rerun()
                        else:
                            st.error("Invalid email or password")

        st.markdown("""
            <div style="text-align: center; margin-top: 25px;">
                <p style="color: #666;">Don't have an account? <a href="?page=register" style="color: var(--primary); font-weight: 500;">Sign up</a></p>
            </div>
        </div>
        """, unsafe_allow_html=True)
