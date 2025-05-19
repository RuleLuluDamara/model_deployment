import numpy as np
import joblib
from tensorflow.keras.models import load_model

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
