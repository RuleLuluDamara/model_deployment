import streamlit as st
from PIL import Image
from utils.helpers import image_to_base64
import hashlib
import time
import numpy as np
import tensorflow as tf
import joblib
from keras.models import load_model
import time
from components.css import load_css
from components.auth import users_db, hash_password
from components.navbar import navbar
from components.login import login_page
from components.register import register_page
from components.predict import predict_page


def main():
    """Main application flow"""
    load_css()
    navbar()

    page = st.query_params.get("page", "predict")

    if page == "login":
        login_page()
    elif page == "register":
        register_page()
    elif page == "logout":
        if 'user' in st.session_state:
            del st.session_state.user
        st.query_params["page"] = "login"
        st.rerun()
    else:
        predict_page()


if __name__ == "__main__":
    main()
