# Food Grading Prediction Web App (with Streamlit)

## This is a web-based app built using **Streamlit** to predict food grading results.

## Features

- Login Page (tanpa database eksternal)
- Prediksi NutriScore berdasarkan 8 nilai gizi:
  Energi
  Protein
  Lemak
  Karbohidrat
  Gula
  Natrium
  Lemak jenuh
  Serat

---

## 📁 Struktur Direktori

```bash
│
├── app.py
│
├── components/
│ ├── navbar.py
│ ├── styles.py
│ ├── css.py
│ ├── login.py
│ ├── navbar.py
│ ├── predict.py
│ ├── register.py
│ └── auth.py
│
├── model/
│ └── predictor.py
│
├── asset/
│ └── logo.png
│
├── pages/
│ ├── login.py
│ ├── register.py
│ └── predict.py
│
├── styles/
│ └── style.py
│
├── model_grade_predict_dum.h5
├── scaler.joblib
├── requirements.txt
└── README.md # Dokumentasi proyek ini
```

## Cara Menjalankan Aplikasi

### 1. 📦 Install Dependencies

Pastikan kamu telah menginstall Python >= 3.7. Kemudian jalankan:

```bash
pip install -r requirements.txt
```

### 2. ▶️ Jalankan Aplikasi

```bash
▶️ Jalankan Aplikasi
```

## Teknologi yang Digunakan

| Tool             | Fungsi                             |
| ---------------- | ---------------------------------- |
| Streamlit        | UI dan Routing                     |
| TensorFlow/Keras | Model deep learning klasifikasi    |
| Joblib           | Menyimpan dan memuat scaler        |
| NumPy            | Manipulasi array                   |
| CSS              | Styling antarmuka                  |
| hashlib          | Hash password untuk login/register |

## Catatan Tambahan

Data user tidak disimpan secara permanen — hanya berada dalam runtime (dictionary users_db).

Kamu bisa menambahkan integrasi database atau autentikasi lanjutan jika diinginkan.

Model model_grade_predict_dum.h5 dan scaler.joblib harus tersedia di root folder agar aplikasi berjalan.

## Preview
![Screenshot 2025-05-20 005103](https://github.com/user-attachments/assets/31575874-76f1-400a-bf74-fa2547049a3f)
![image](https://github.com/user-attachments/assets/291b98a5-f239-4eb5-be3d-23035df9fba4)

