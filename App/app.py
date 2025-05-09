import streamlit as st
import numpy as np
import pandas as pd
import joblib  # Untuk memuat model

# Muat model jika sudah ada (ganti dengan path model Anda)
# model = joblib.load("model.pkl")

# Judul aplikasi
st.set_page_config(page_title="Food Grading Prediction",
                   page_icon="🥬", layout="centered")

st.title("🥬 Food Grading Prediction")
st.markdown("Masukkan data makanan untuk memprediksi tingkat kualitasnya.")

# Form input
with st.form("grading_form"):
    moisture = st.number_input(
        "Kadar Air (%)", min_value=0.0, max_value=100.0, step=0.1)
    weight = st.number_input("Berat (gram)", min_value=0.0, step=1.0)
    sugar = st.number_input(
        "Kadar Gula (%)", min_value=0.0, max_value=100.0, step=0.1)
    color_score = st.slider(
        "Skor Warna (1 = buruk, 10 = sangat baik)", 1, 10, 5)

    submitted = st.form_submit_button("Prediksi")

# Proses prediksi
if submitted:
    # Contoh data sebagai array
    input_data = np.array([[moisture, weight, sugar, color_score]])

    # Jika model tersedia
    # prediction = model.predict(input_data)
    # grade = prediction[0]

    # Dummy output untuk contoh
    grade = "A" if moisture < 50 and sugar > 10 and color_score > 7 else "B"

    st.success(f"Prediksi Tingkat Kualitas: **Grade {grade}**")

    # Tambahkan penjelasan atau rekomendasi
    st.markdown(
        f"""
        ### ℹ️ Informasi Tambahan:
        - Kadar Air: `{moisture}%`
        - Kadar Gula: `{sugar}%`
        - Warna: `{color_score}/10`
        """
    )
