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

users_db = {
    "rule": {
        "name": "Admin",
        # sha256 of "password"
        "password": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"
    }
}


def load_css():
    st.markdown("""
    <style>
        :root {
            --primary: #2e8b57;
            --secondary: #3aa76d;
            --accent: #f4a261;
            --light: #f8f9fa;
            --dark: #343a40;
            --danger: #dc3545;
        }
        
        /* Main container */
        .stApp {
            background-color: #f5f5f5;
        }
        
        /* Navbar */
        .navbar {
            height: 80px;
            width: 100%;
            background: white;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid #e6e6e6;
            margin-top: 40px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            padding: 0 20px;
        }
        .navbar-brand {
            display: flex;
            align-items: center;
        }
        .navbar-logo {
            height: 40px;
            margin-right: 10px;
        }
        .navbar-title {
            font-size: 24px;
            font-weight: bold;
            color: var(--primary);
            font-family: 'Arial Rounded MT Bold', sans-serif;
        }
        .navbar-items {
            display: flex;
        }
        .nav-item {
            padding: 10px 20px;
            margin: 0 5px;
            cursor: pointer;
            border-radius: 30px;
            transition: all 0.3s ease;
            color: var(--dark);
            text-decoration: none;
            font-weight: 500;
        }
        .nav-item:hover {
            background-color: rgba(46, 139, 87, 0.1);
            color: var(--primary);
        }
        .nav-item.active {
            background-color: var(--primary);
            color: white !important;
            box-shadow: 0 4px 6px rgba(46, 139, 87, 0.2);
        }
        
        /* Cards */
        .card {
            background: white;
            border-radius: 12px;
            padding: 25px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            margin-bottom: 20px;
        }
        
        /* Forms */
        .form-container {
            max-width: 500px;
            margin:  10px auto;
            padding: 30px;
            background: white;
            border-radius: 12px;

            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        }
        .form-title {
            color: var(--primary);
            text-align: center;
            margin-bottom: 15px;
            font-size: 24px;
            font-weight: 500;
        }
        .form-input {
            max-width: 500px;
            padding: 25px;
            margin-bottom: 20px;
        }
        .form-input label {
            display: block;
            margin-bottom: 8px;
            font-weight: 500;
            color: var(--dark);
        }
        .form-input input {
            width: 50%;
            padding: 12px 15px;
            border: 1px solid #ddd;
            border-radius: 8px;
            font-size: 16px;
            transition: all 0.3s;
        }
        .form-input input:focus {
            border-color: var(--primary);
            box-shadow: 0 0 0 3px rgba(46, 139, 87, 0.2);
            outline: none;
        }
        .submit-btn {
            width: 100%;
            padding: 12px;
            background-color: var(--primary);
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.3s;
            margin-top: 10px;
        }
        .submit-btn:hover {
            background-color: var(--secondary);
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(46, 139, 87, 0.3);
        }
        
        /* Animations */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .animated {
            animation: fadeIn 0.5s ease-out;
        }
        
        /* Nutriscore display */
        .nutriscore {
            font-size: 24px;
            font-weight: bold;
            width: 70px;
            height: 70px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 50%;
            color: white;
            margin: 20px auto;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        
        /* Footer */
        .footer {
            text-align: center;
            margin-top: 50px;
            padding: 20px;
            color: #666;
            font-size: 14px;
        }
                
        .centered-form {
            max-width: 400px;
            margin: 80px auto 40px auto; /* atas, kanan-kiri, bawah */
            background: white;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        }
                
        .block-container {
            padding: 0 !important;
            margin: 0 !important;
            max-width: 100% !important;
        }
                

    </style>
    """, unsafe_allow_html=True)


def navbar():
    """Render the navigation bar with logo and menu items"""
    logo_path = "asset/logo.png"
    logo = Image.open(logo_path)

    current_page = st.query_params.get("page", "predict")

    if 'user' in st.session_state:
        auth_target = "logout"
        auth_label = "Logout"
    else:
        auth_target = "login"
        auth_label = "Login"

    st.markdown(f"""
    <div class="navbar animated">
        <div class="navbar-brand">
            <img class="navbar-logo" src="data:image/png;base64,{image_to_base64(logo)}">
            <div class="navbar-title">NutriOMatic</div>
        </div>
        <div class="navbar-items">
            <div class="nav-item {'active' if current_page == 'predict' else ''}" 
                 onclick="window.location.href='?page=predict'">Scan Product</div>
            <div class="nav-item {'active' if current_page == 'login' else ''}" 
                 onclick="window.location.href='?page={'logout' if 'user' in st.session_state else 'login'}'">
                 {'Logout' if 'user' in st.session_state else 'Login'}
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


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


model = load_model('model_grade_predict_dum.h5')
scaler = joblib.load('scaler.joblib')


def predict_nutriscore(energy_100g, proteins_100g, fat_100g, carbohydrates_100g, sugars_100g, sodium_100g, saturated_fat_100g, fiber_100g):
    X = np.array([[energy_100g, proteins_100g, fat_100g, carbohydrates_100g,
                 sugars_100g, sodium_100g, saturated_fat_100g, fiber_100g]])
    X_scaled = scaler.transform(X)
    nutriscore_grade_pred = model.predict(X_scaled)
    predicted_grade = np.argmax(nutriscore_grade_pred, axis=-1)
    mapping = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E'}
    return mapping[predicted_grade[0]]


def predict_page():
    if 'user' not in st.session_state:
        st.query_params["page"] = "login"
        st.rerun()

    st.markdown(f"""
    <div class="card animated">
        <h2 style="color: var(--primary); text-align: center;">Hello, {st.session_state.user['name']}! 👋</h2>
        <p style="text-align: center; color: #666;">Input product nutritional values to get NutriScore grade</p>
    </div>
    """, unsafe_allow_html=True)

    with st.container():
        cols = st.columns([1, 2, 1])
        with cols[1]:
            with st.form("nutrition_form"):
                st.markdown("""
                <div class="card">
                    <h3 style="color: var(--primary);">Nutrition Input</h3>
                """, unsafe_allow_html=True)

                energy = st.number_input(
                    'Energy (kcal) per 100g', min_value=0.0, step=0.1)
                proteins = st.number_input(
                    'Proteins per 100g', min_value=0.0, step=0.1)
                fat = st.number_input('Fat per 100g', min_value=0.0, step=0.1)
                carbohydrates = st.number_input(
                    'Carbohydrates per 100g', min_value=0.0, step=0.1)
                sugars = st.number_input(
                    'Sugars per 100g', min_value=0.0, step=0.1)
                sodium = st.number_input(
                    'Sodium per 100g', min_value=0.0, step=0.1)
                saturated_fat = st.number_input(
                    'Saturated Fat per 100g', min_value=0.0, step=0.1)
                fiber = st.number_input(
                    'Fiber per 100g', min_value=0.0, step=0.1)

                submit = st.form_submit_button(
                    "Analyze Product", type="primary")

                st.markdown("</div>", unsafe_allow_html=True)

                if submit:
                    with st.spinner("Analyzing nutrition..."):
                        time.sleep(2)
                        prediction = predict_nutriscore(
                            energy, proteins, fat, carbohydrates, sugars,
                            sodium, saturated_fat, fiber
                        )
                        color_map = {'A': '#009966', 'B': '#85BB2F',
                                     'C': '#FFCC00', 'D': '#FF9933', 'E': '#CC0033'}
                        desc_map = {
                            'A': 'Excellent Nutritional Quality',
                            'B': 'Good Nutritional Quality',
                            'C': 'Moderate Nutritional Quality',
                            'D': 'Poor Nutritional Quality',
                            'E': 'Very Poor Nutritional Quality'
                        }

                        st.success("Analysis complete!")

                        st.markdown(f"""
                        <div style="margin-top: 30px;">
                            <h3 style="color: var(--primary);">Analysis Result</h3>
                            <div class="nutriscore" style="background: {color_map[prediction]}; font-size: 64px; text-align: center; color: white; border-radius: 8px; padding: 20px; width: 100px; margin: 0 auto;">{prediction}</div>
                            <p style="text-align: center; font-size: 18px; font-weight: 600;">{desc_map[prediction]}</p>
                        </div>
                        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="footer">
        <p>© 2023 NutriScan | Eat Healthy, Live Better</p>
    </div>
    """, unsafe_allow_html=True)


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
