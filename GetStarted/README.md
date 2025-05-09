# Streamlit App Setup Guide

This guide will help you set up and run the Streamlit application locally.

---

## Understanding Streamlit's client-server architecture

Streamlit apps have a client-server structure. The Python backend of your app is the server. The frontend you view through a browser is the client.

### Python backend (server)

The machine running your Streamlit server is also called a host. When you execute the command `streamlit run app.py`, your computer uses Python to start up a Streamlit server.

### Python frontend (client)

When someone views your app through a browser, their device is a Streamlit client. When you view your app from the same computer where you are running or developing your app, then server and client are coincidentally running on the same machine.

## Prerequisites

Make sure you have the following installed:

- Python 3.9+
- pip (Python package installer)

### Project Structure

```bash
project_name/
│
├── app.py
├── requirements.txt
├── README.md
└── kppl_rka/
```

## 1. Create and Activate Virtual Environment

Open a terminal and navigate to your project folder

```bash
cd project_name
```

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

## A folder named ".kppl_rka" will appear in your project. This directory is where your virtual environment and its dependencies are installed.

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

![image](https://github.com/user-attachments/assets/c4ae211a-909b-4c9e-9159-df3345344688)

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
