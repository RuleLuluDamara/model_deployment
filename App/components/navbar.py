import streamlit as st
from PIL import Image
from utils.helpers import image_to_base64

def navbar():
    """Render the navigation bar with logo and menu items"""
    logo_path = "asset/logo.png"
    logo = Image.open(logo_path)
    
    # Get current page from query params
    current_page = st.query_params.get("page", "predict")
    
    # CSS styling
    st.markdown("""
    <style>
        .navbar {
            height: 80px;
            width: 100%;
            background: white;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid #e6e6e6;
            margin-bottom: 30px;
        }
        .navbar-brand {
            display: flex;
            align-items: center;
            margin-left: 20px;
        }
        .navbar-logo {
            height: 40px;
            margin-right: 10px;
        }
        .navbar-title {
            font-size: 24px;
            font-weight: bold;
            color: #2e8b57;
        }
        .navbar-items {
            display: flex;
            margin-right: 20px;
        }
        .nav-item {
            padding: 10px 15px;
            margin: 0 5px;
            cursor: pointer;
            border-radius: 5px;
            transition: all 0.3s ease;
            color: #333;
            text-decoration: none;
        }
        .nav-item:hover {
            background-color: #f0f0f0;
        }
        .nav-item.active {
            background-color: #2e8b57;
            color: white !important;
        }
    </style>
    """, unsafe_allow_html=True)

    # Navbar HTML
    st.markdown(f"""
    <div class="navbar">
        <div class="navbar-brand">
            <img class="navbar-logo" src="data:image/png;base64,{image_to_base64(logo)}">
            <div class="navbar-title">Nutriscore Predictor</div>
        </div>
        <div class="navbar-items">
            <div class="nav-item {'active' if current_page == 'predict' else ''}" 
                 onclick="window.location.href='?page=predict'">Predict</div>
            <div class="nav-item {'active' if current_page == 'login' else ''}" 
                 onclick="window.location.href='?page=login'">Login</div>
        </div>
    </div>
    """, unsafe_allow_html=True)