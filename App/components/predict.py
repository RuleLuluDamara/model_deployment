import streamlit as st
import time
from model.predictor import predict_nutriscore


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
