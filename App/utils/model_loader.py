import numpy as np
import joblib
import tensorflow as tf
from keras.models import load_model
import streamlit as st


@st.cache_resource
def load_models():
    model = load_model('model_grade_predict_dum.h5')
    scaler = joblib.load('scaler.joblib')
    return model, scaler


model, scaler = load_models()


def predict_nutriscore(energy_100g, proteins_100g, fat_100g, carbohydrates_100g,
                       sugars_100g, sodium_100g, saturated_fat_100g, fiber_100g):
    """Predict nutriscore grade from nutritional values"""
    X = np.array([[energy_100g, proteins_100g, fat_100g, carbohydrates_100g,
                 sugars_100g, sodium_100g, saturated_fat_100g, fiber_100g]])
    X_scaled = scaler.transform(X)
    nutriscore_grade_pred = model.predict(X_scaled)
    predicted_class = np.argmax(nutriscore_grade_pred, axis=-1)[0]
    mapping = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E'}
    return mapping[predicted_class]
