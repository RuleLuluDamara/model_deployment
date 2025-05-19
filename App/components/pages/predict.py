import streamlit as st
from utils.model_loader import predict_nutriscore


def show():
    """Render the prediction page"""
    st.title("Nutriscore Grade Prediction")
    st.markdown(
        "Masukkan nilai nutrisi per 100g untuk memprediksi **Nutriscore Grade (A–E)** produk makanan.")

    st.markdown("---")

    with st.form("nutriscore_form"):
        st.subheader("🧪 Input Nutritional Values")
        col1, col2 = st.columns(2)

        with col1:
            energy_100g = st.number_input(
                'Energy (kcal)', min_value=0.0, step=0.1)
            proteins_100g = st.number_input(
                'Proteins (g)', min_value=0.0, step=0.1)
            fat_100g = st.number_input('Fat (g)', min_value=0.0, step=0.1)
            fiber_100g = st.number_input('Fiber (g)', min_value=0.0, step=0.1)

        with col2:
            carbohydrates_100g = st.number_input(
                'Carbohydrates (g)', min_value=0.0, step=0.1)
            sugars_100g = st.number_input(
                'Sugars (g)', min_value=0.0, step=0.1)
            sodium_100g = st.number_input(
                'Sodium (mg)', min_value=0.0, step=0.1)
            saturated_fat_100g = st.number_input(
                'Saturated Fat (g)', min_value=0.0, step=0.1)

        submitted = st.form_submit_button("🔍 Predict")

    if submitted:
        grade = predict_nutriscore(
            energy_100g, proteins_100g, fat_100g, carbohydrates_100g,
            sugars_100g, sodium_100g, saturated_fat_100g, fiber_100g
        )

        st.markdown("### 📊 Hasil Prediksi")
        st.success(f"🎯 Nutriscore Grade yang diprediksi adalah: **{grade}**")

        st.markdown("---")
        st.markdown("""
        **Keterangan Grade:**
        - 🟢 **A**: Sangat sehat
        - 🟡 **B / C**: Sedang
        - 🔴 **D / E**: Perlu dibatasi konsumsinya
        """)
