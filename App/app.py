import streamlit as st
import numpy as np
import tensorflow as tf
from keras.models import load_model
import joblib

model_load = load_model('model_grade_predict_dum.h5')
scaler_load = joblib.load('scaler.joblib')

def predict_nutriscore(energy_100g, proteins_100g, fat_100g, carbohydrates_100g,
                       sugars_100g, sodium_100g, saturated_fat_100g, fiber_100g):
    X = np.array([[energy_100g, proteins_100g, fat_100g, carbohydrates_100g,
                   sugars_100g, sodium_100g, saturated_fat_100g, fiber_100g]])
    X_scaled = scaler_load.transform(X)
    nutriscore_grade_pred = model_load.predict(X_scaled)
    predicted_class = np.argmax(nutriscore_grade_pred, axis=-1)[0]
    mapping = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E'}
    return mapping[predicted_class]


st.set_page_config(page_title="Nutriscore Predictor",
                   page_icon="🥦", layout="centered")

st.title("🥦 Nutriscore Grade Predictor")
st.markdown(
    "Masukkan nilai nutrisi per 100g untuk memprediksi **Nutriscore Grade (A–E)** produk makanan.")

st.markdown("---")

with st.form("nutriscore_form"):
    st.subheader("🧪 Input Nutritional Values")
    col1, col2 = st.columns(2)

    with col1:
        energy_100g = st.number_input('Energy (kcal)', min_value=0.0, step=0.1)
        proteins_100g = st.number_input(
            'Proteins (g)', min_value=0.0, step=0.1)
        fat_100g = st.number_input('Fat (g)', min_value=0.0, step=0.1)
        fiber_100g = st.number_input('Fiber (g)', min_value=0.0, step=0.1)

    with col2:
        carbohydrates_100g = st.number_input(
            'Carbohydrates (g)', min_value=0.0, step=0.1)
        sugars_100g = st.number_input('Sugars (g)', min_value=0.0, step=0.1)
        sodium_100g = st.number_input('Sodium (mg)', min_value=0.0, step=0.1)
        saturated_fat_100g = st.number_input(
            'Saturated Fat (g)', min_value=0.0, step=0.1)

    submitted = st.form_submit_button("🔍 Predict")

if submitted:
    grade = predict_nutriscore(energy_100g, proteins_100g, fat_100g, carbohydrates_100g,
                               sugars_100g, sodium_100g, saturated_fat_100g, fiber_100g)

    st.markdown("### 📊 Hasil Prediksi")
    st.success(f"🎯 Nutriscore Grade yang diprediksi adalah: **{grade}**")

    st.markdown("---")
    st.markdown("""
    **Keterangan Grade:**
    - 🟢 **A**: Sangat sehat
    - 🟡 **B / C**: Sedang
    - 🔴 **D / E**: Perlu dibatasi konsumsinya
    """)
