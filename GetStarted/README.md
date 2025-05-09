# Streamlit App Setup Guide

This guide will help you set up and run the Streamlit application locally.

---

## Prerequisites

Make sure you have the following installed:

- Python 3.7+
- pip (Python package installer)

### Project Structure

```bash
project-folder/
│
├── app.py
├── requirements.txt
├── README.md
└── venv/
```

## 1. Create and Activate Virtual Environment

### Windows (Command Prompt / PowerShell)

```bash
python -m venv kppl_rka
kppl_rka\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv kppl_rka
source kppl_rka/bin/activate
```

---

## 2. Install Streamlit and Dependencies

Install Streamlit and other required libraries:

```bash
pip install streamlit
pip install pandas numpy matplotlib seaborn
```

If using requirements.txt, run:

```bash
pip install -r requirements.txt
```

Validate the installation by running our Hello app:

```bash
streamlit hello
```

---

## 3. Run the Streamlit App

Make sure you're in the directory where your Streamlit app (e.g., app.py) is located. Then run:

```bash
streamlit run app.py
```

The app will open in your browser at:

```bash
http://localhost:8501
```

---

## 3. Stop the App

To stop the Streamlit server, press:

```bash
CTRL + C
```

---

## Notes

If your app needs access to databases or APIs, make sure required credentials or .env files are set up.

To exit the virtual environment, simply type:

```bash
deativate
```

---
